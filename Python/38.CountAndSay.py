class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def convert(arr):
            result = ''
            for digit, count in arr:
                result += str(count) + str(digit)
            return result
        
        def RLE(n):
            number = str(n)
        
            if not number: return []

            arr = []
            curr = number[0]
            counter = 1

            for digit in number[1:]:
                if digit == curr:
                    counter += 1
                else:
                    arr.append([curr, counter])
                    curr = digit
                    counter = 1

            arr.append([curr, counter])
            return arr  

        result = "1"
        for _ in range(1,n):
            result = convert(RLE(result))
        return result


    

    
