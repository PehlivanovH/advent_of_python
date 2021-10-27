class PasswordVerifier:

    def verifyPasswordList(self, input):
        correctPwds = 0;

        for pwd in input:
            if self.pwdCorrect(pwd):
                correctPwds += 1;

        return correctPwds

    def pwdCorrect(self, input):
        inputs = input.split()
        rule = inputs[0]
        letter = inputs[1]
        pwd = inputs[2]
        ruleParts = rule.split('-')
        ruleMin = int(ruleParts[0])
        ruleMax = int(ruleParts[1])

        letterCountInPwd = pwd.count(letter[0])
        if letterCountInPwd >= ruleMin and letterCountInPwd <= ruleMax:
            return True;

        return False;
