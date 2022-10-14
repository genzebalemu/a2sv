lass Solution(object):
    def compress(self, chars):
        i=index=0
        while i<len(chars):
            l =i
            while l < len(chars) and chars[i]==chars[l]:
                l +=1
            chars[index]=chars[i]
            index +=1
            count =l-i
            if count >1:
                for c in str(count):
                    chars[index]=c
                    index +=1
            i=l
        chars = chars[:index]
        return index