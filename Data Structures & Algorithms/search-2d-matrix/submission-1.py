class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        t,b = 0, len(matrix)-1
        l,r = 0, len(matrix[0]) -1

        while t<b:
            mid = int(t+ (b-t)/2)

            if target < matrix[mid][-1]:
                b = mid
            elif target > matrix[mid][-1]:
                t = mid +1
            else:
                return True

        # now t = b


        nums = matrix[t]
        print(nums)
        while l <= r:
            mid = int(l + (r-l)/2)

            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
            else:
                return True
        return False        
        