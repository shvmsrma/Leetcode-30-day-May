#An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

#Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

#To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. 
#Replace the color of all of the aforementioned pixels with the newColor.

#At the end, return the modified image.




def changeColor(self, image, i, j, nC,oC):
        if image[i][j]!=oC:
            return
        image[i][j]=nC
        if i!=0:
            self.changeColor(image,i-1,j,nC,oC)
        if j!=0:
            self.changeColor(image,i,j-1,nC,oC)
        if i!=len(image)-1:
            self.changeColor(image,i+1,j,nC,oC)
        if j!=len(image[0])-1:
            self.changeColor(image,i,j+1,nC,oC)

        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        self.changeColor(image,sr,sc,newColor, oldColor)
        return image
