# Написать функцию is_isogram, определяющую является ли заданное слово
# изограмом, т.е. словом, в котором ни одна буква не повторяется больше
# одного раза, в независимости от регистра
#
# Примеры:
# is_isogram("documentary" ) ==> true
# is_isogram("abA" ) ==> false


class words:
    def origin_word(self, s):
        self = True
        if len(s) < 2:
            return True
        else:
            for i in range(0, len(s)):
                if not self:
                    break
                for j in range(i + 1, len(s)):
                    if not self:
                        break
                    if (ord(s[i]) - ord(s[j]) == 32) or (ord(s[i]) - ord(s[j]) == -32) or (ord(s[i]) - ord(s[j])) == 0:
                        self = False
            return self

# Тесты
# try:
#   assert is_isogram("Dermatoglyphics") == True
#  assert is_isogram("isogram") == True
# assert is_isogram("granulocytes") == True
# assert is_isogram("moOse") == False
# assert is_isogram("isIsogram") == False
# assert is_isogram("") == True
