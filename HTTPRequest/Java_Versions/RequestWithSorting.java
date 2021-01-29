import java.net.HttpURLConnection;
import java.net.URL;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;
import javafx.util.Pair;

class Result {

    public static HttpURLConnection connection;
    private static double numPages = Double.POSITIVE_INFINITY;

    public static ArrayList<Pair<String, Long>> parseJson(String response) {
        ArrayList<Pair<String, Long>> result = new ArrayList();
        try {
            Object obj = new JSONParser().parse(response);
            JSONObject jsonObj = (JSONObject) obj;
            long totalPages = (long) jsonObj.get("total_pages");
            numPages = (double) totalPages;

            JSONArray data = (JSONArray) jsonObj.get("data");
            Iterator authorIter = data.iterator();

            while (authorIter.hasNext()) {
                JSONObject author = (JSONObject) authorIter.next();
                String titleName = (String) author.get("title");
                String storyTitle = (String) author.get("story_title");
                Long numComments = (Long) author.get("num_comments");
                if (numComments == null) {
                    numComments = 0L;
                }

                if (titleName != null) {
                    result.add(new Pair <String, Long>(titleName, numComments));
                }
                else if (storyTitle != null) {
                    result.add(new Pair <String, Long>(storyTitle, numComments));
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return result;
    }

    public static List<Pair<String, Long>> fetchJson(String username, int page) {
        ArrayList<Pair<String, Long>> result = new ArrayList();
        BufferedReader reader;
        String line;
        StringBuffer responseContent = new StringBuffer();

        try {
            URL url = new URL("https://jsonmock.hackerrank.com/api/articles?author=" + username + "&page=" + Integer.toString(page));
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setConnectTimeout(5000);
            connection.setReadTimeout(5000);

            reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            while ((line = reader.readLine()) != null) {
                responseContent.append(line);
            }
            reader.close();

            String resp = responseContent.toString();
            result.addAll(parseJson(resp));
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            connection.disconnect();
        }

        return result;
    }

    public static List<String> topArticles(String username, int limit)
    {
        ArrayList<String> result = new ArrayList();
        ArrayList<Pair<String, Long>> intermediate = new ArrayList();

        int max_limit = limit;
        int page = 1;
        while (page <= numPages) {
            intermediate.addAll(fetchJson(username, page));
            page++;
        }


        intermediate.sort(new Comparator<Pair<String, Long>>() {
            @Override
            public int compare(Pair<String, Long> o1, Pair<String, Long> o2) {
                if (o1.getValue() > o2.getValue()) {
                    return -1;
                } else if (o1.getValue().equals(o2.getValue())) {
                    return o1.getKey().compareTo(o2.getKey());
                } else {
                    return 1;
                }
            }
        });


        for (Pair<String,Long> temp : intermediate)
        {
            if (max_limit == 0) {
                break;
            }

            result.add(temp.getKey());
            max_limit--;
        }

        return result;
    }

}

