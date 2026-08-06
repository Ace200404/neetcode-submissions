class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows,Cols=len(matrix),len(matrix[0])

        top,bottom=0,Rows-1

        while top<=bottom:
            row = (top+bottom)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                break
        row=(top+bottom)//2
        
        l,r=0,Cols-1

        while l<=r:
            middle=(l+r)//2
            if target>matrix[row][middle]:
                l=middle+1
            elif target< matrix[row][middle]:
                r=middle-1
            else:
                return True
        return False
