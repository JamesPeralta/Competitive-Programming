import java.net.HttpURLConnection;
import java.net.URL;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;
import javafx.util.Pair;

class Result {
    private static HttpURLConnection connection;
    private static double numPages = Double.POSITIVE_INFINITY;

    private static List<Pair<String, Long>> parseJson(String input) {
        ArrayList<Pair<String, Long>> result = new ArrayList();
        try {
            Object obj = new JSONParser().parse(input);
            JSONObject jsonObj = (JSONObject) obj;
            long totalPages = (long) jsonObj.get("total_pages");
            numPages = (double) totalPages;

            JSONArray data = (JSONArray) jsonObj.get("data");
            Iterator authorIter = data.iterator();

            while (authorIter.hasNext()) {
                JSONObject author = (JSONObject) authorIter.next();
                String authorName = (String) author.get("username");
                long submissions = (long) author.get("submission_count");
                result.add(new Pair <String, Long> (authorName, submissions));
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }

        return result;
    }

    private static ArrayList<String> fetchJson(int page, int threshold) {
        ArrayList<String> result = new ArrayList();

        BufferedReader reader;
        String line;
        StringBuffer responseContent = new StringBuffer();
        try {
            URL url = new URL("https://jsonmock.hackerrank.com/api/article_users?page=" + Integer.toString(page));
            connection = (HttpURLConnection) url.openConnection();

            connection.setRequestMethod("GET");
            connection.setConnectTimeout(5000);
            connection.setReadTimeout(5000);

            int status = connection.getResponseCode();

            if (status > 299) {
                reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
                while ((line = reader.readLine()) != null) {
                    responseContent.append(line);
                }
                reader.close();
            } else {
                reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                while ((line = reader.readLine()) != null) {
                    responseContent.append(line);
                }
                reader.close();
            }

            String resp = responseContent.toString();
            List<Pair<String, Long>> res = parseJson(resp);
            for (Pair<String,Long> temp : res)
            {
                if (temp.getValue() > threshold)
                {
                    result.add(temp.getKey());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            connection.disconnect();
        }

        return result;
    }

    public static List<String> getUsernames(int threshold) {
        ArrayList<String> result = new ArrayList();
        int page = 1;
        while (page <= numPages) {
            result.addAll(fetchJson(page, threshold));
            page++;
        }
        return result;
    }
}

