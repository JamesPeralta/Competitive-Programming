class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block_comment = False
        output = []

        output_str = []
        for line in source:
            line = list(line)

            i = 0
            while i <= len(line) - 1:
                if "".join(line[i:i + 2]) == "//" and block_comment is False:
                    break
                elif "".join(line[i:i + 2]) == "/*" and block_comment is False:
                    block_comment = True
                    i += 2
                    continue
                elif "".join(line[i:i + 2]) == "*/" and block_comment is True:
                    block_comment = False
                    i += 2
                    continue
                elif block_comment is False:
                    output_str.append(line[i])

                i += 1

            if "".join(output_str) != "" and block_comment is False:
                output.append("".join(output_str))
                output_str = []

        return output