from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         strings are immutable so we can easily use that as hash keys but so are tuples and they are very easy to create
# dict.keys() and dict.values() both return a list

        result = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            result[tuple(count)].append(string)
        
        return result.values()
        
#     def getFrequencies(self,string):
#         frequency = defaultdict(lambda: 0)
#         for char in string:
#             frequency[char] += 1
#             # pythonic way without using defaultdict from collections is .get()
#         return frequency
        
    
#     def getKeyString(self,frequency):
#         tempKey = ""
#         for key,value in frequency.items():
#             tempKey += f"{key}{value}"
#         return tempKey
    
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # subroutine checkAnagrams(string1,string2) returns if two strings are anagrams
#         # the key of a dictionary has to be immutable, i.e, only ints, strings, bools
#         # subroutine to take a string, get the frequencies and convert that into a string key
#         # iterate over list of strs to find frequencies, compare if keyStr exists in visited
#         # append result to value of key if equal
#         # O(N) to iterate over list of strs, O(M) to iterate over the longest string in list -> total time complexity is O(N*M) space and time
#         # dictionary after python 3.7 stores the order in the order it was inserted so sorting might be required for the logic to work 
#         visited = {}
#         result = []
#         for string in strs:
#             sorted_string = ''.join(sorted(string))
#             currentKeyString = self.getKeyString(self.getFrequencies(sorted_string))
#             if currentKeyString in visited:
#                 visited[currentKeyString].append(string)
#             else:
#                 visited[currentKeyString]  = [string]
        
#         for key, value in visited.items():
#             result.append(value)
#         return result
    
    
    