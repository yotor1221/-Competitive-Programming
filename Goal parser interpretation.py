class Solution:
    def interpret(self, command: str) -> str:
        goal_parser = {"G": "G", "()": "o", "(al)": "al"}
        result_value = []
        i = 0
        while i < len(command):
            if i + 3 < len(command) and command[i:i+4] == "(al)":
                key = command[i:i+4]
                result_value.append(goal_parser[key])
                i += 4
            elif i + 1 < len(command) and command[i:i+2] == "()":
                key = command[i:i+2]
                result_value.append(goal_parser[key])
                i += 2
            else:
                key = command[i]
                result_value.append(goal_parser[key])
                i += 1
        return "".join(result_value)
