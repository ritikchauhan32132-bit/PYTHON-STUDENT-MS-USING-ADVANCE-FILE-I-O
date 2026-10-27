import time
import numpy as np

start = time.perf_counter()

# arr = np.arange(1, 1000000)
# arr = np.round(arr * 2.5)

# print(arr[:10])

# # QR code generate by UPI ID usiing python
# import qrcode
# from urllib.parse import urlencode

# upi_id = "7814410991-3@nyes"
# name = "Ritik Kumar"

# data = "upi://pay?" + urlencode({
#     "pa": upi_id,
#     "pn": name,
#     "cu": "INR"
# })

# qr = qrcode.make(data)
# qr.save("payment_qr.png")

# print("UPI Payment QR Generated Successfully!")



import numpy as np

arr = np.arange(1,11)

# print(arr)

arr = np.arange(1,10).reshape(3,3)
# print("\n",arr)

a1 = np.array([1,2,3], dtype=str)
# print(a1)
# print(type(a1))

a2 = np.arange(1,11).reshape(2,5)
# print(a2)

a3 = np.ones((3,4))
# print(a3)

a4 = np.zeros((3,4))
# print(a4)


a5 = np.random.random((3,4))
# print(a5.dtype)


a6 = np.linspace(10,100,9).reshape(3,3)
# print(a6)

a7 = np.identity(3)
# print(a7)

# print(a6.ndim)

# print(a6.shape)

# print(a6.size)

# print(a6.itemsize)

# a = 78

a1 = np.array([[[2,4,7],[5,6,8]]])
a2 = np.array([[1,4],[2,5],[3,6]])
# print(a1,"\n",a2)

# print(np.dot(a1,a2))
# print(np.log(a2))

b = np.round(np.random.random((2,3))*100)
# print(b)

# import qrcode as qr
# img = qr.make("https://www.google.com/search?q=india+me+junior+DATA+SCINCE+ENGINEER+ka+average+salary+kitna+hai%3F&oq=india+me+junior+DATA+SCINCE+ENGINEER+ka+average+salary+kitna+hai%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRiPAjIHCAIQIRiPAtIBCTM0MjUxajBqN6gCALACAA&sourceid=chrome&source=chrome.ob&ie=UTF-8&mstk=AUtExfB6OtnEmTmDwsrshMwA9RK2izi8kRVeoPhWiJgWo8lLjWPE8FjzObf2icJPI5d0OoDKn95cUJltOVcWuRdrHnEGsOJ-roFCYlm68-eGc6m6CvDubl8RuDoL1RxG4kIqEb3t4-kf9t7DsCrQlIwVw_CvraORmHaRlMNyb0TBXn0CYHo1jcstcCjj-nqWP2OmQBC2Veo-aNuoSTjnYAwT63yPfTX74B1dK42b4qw2aMay3rughK8BsYlpXAbj9Sn839lcyoOpG1NnfVulx0ncj17Hb0IAPDYkdRrx3Oc0ZCc1-MTYew&csuir=1&aioh=3&udm=50#aof=1")
# img.save("meraqr.png")

# qra = qr.make("https://reelsbaba.com/search/girls/")
# print("QR Code Generating....")
# qra.save("link.png")


# 1d Array
d1 = np.array([1,2,3,4,5,6,7,8,9,0])
# print(d1)

# 2d Array
d2 = np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(d2)

d3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(d3)

# import qrcode as mr

# phonepay = mr.make("qr.png")

# print("QR Code Generating....")
# phonepay.save("ppay.png")
# print("QR Code Generated Successfully!")



# print(np.shape(d3))
# # ZEROS OR ONES ME TUUPPLE KE FORM ME SHAPE PASS KIYA JATA HAI
zeros = np.zeros((2,3))
# print(zeros)

ones = np.ones((3,4))
# print(ones)


# # jis value se chahhe us value se array bana sakte hai
file = np.full((1,10),2)
# print(file)

# #ARANGE METHOD SE ARRAY CREATING
arang = np.arange(1,10,2)
# print(arang)

iden = np.eye(3)
# print(iden)

# print(iden)
# print(iden.dtype)


## RANDOM METHOD SE ARRAY CREATE KARNA
random = np.random.random((3,4))
# print(random)


## LINESPACE KA UUSE KARKKE ARRAYY CREATE KARNA  MIK9
arr = np.linspace(2,5,2,dtype=int)
# print(arr)






#   <-- YAHA SE FIR SE PRECTICE START KARTE HAI 0 SE NumPY -->


import numpy as np

d1 = np.array([1,2,3,4,5,6])
# print(d1)

d2 = np.array([[1,2,3],
              [4,5,6]])
# print(d2)

d3 = np.array([[[1,2,3],
                 [4,5,6]],
                 [[9,8,7],
                 [5,4,3]]])
# print(d3)


#   <==== YAHA SE KARTE HAI START ===>

# CREATING THE ARRAY

d1 = np.array([1,2,3])
d2 = np.array([[1,2,3],
              [4,5,6]])

d3 = np.array([[[1,2,3],
                [4,5,6]],
               [[9,8,7],
                [5,4,3]]])
# print(d3)

# print(np.shape(d3))


a = np.full((2,3),18)
# print(a)

a = np.arange(12).reshape(2,2,3)
# print(a)


a = np.eye(3)
# print(a)

a = np.zeros((10,12))
# print(a)

a = np.ones((10,12))
# print(a)

a = np.full((10,12),19)
# print(a)


a = np.linspace(-10,10,10)
# print(a)

a = np.eye(3,6, k=1)
# print(a)
a = np.identity(3)
# print(a)

# print(d3.ndim)

# print(d3.shape)
# print(d3.size)

# print(d3.itemsize)
# print(d3.astype(np.int32))
# print(d3.dtype)

# print(np.max(d3))
# print(np.min(d3))
# print(np.sum(d3))


# print(np.max(d3,axis=1)) # Row = 1
# print(np.max(d3,axis=0)) # Column = 0

# print(np.mean(d3))
# print(np.median(d3))
# print(np.std(d3))
# print(dir(np))
# print(np.var(d3))
# print(np.dot(d1,a))
# print(np.log(d3))
# print(np.exp(d3))
# print(np.round(d3))
# print(np.mean(d3))

# for i in d3:
#     print(i)

# for i in np.nditer(d3):
#     print(i)

# print(d3.T)
# print(np.ravel(d3))
# print(np.hstack((d3,d2)))
# print(np.vstack((d3,d2)))
# print(np.hsplit((d3,d2)))
# print(np.vsplit((d3,d2)))

#  <=== ADVANCE INDEXING ===>

a = np.array([[[1,2,3],
               [4,5,6]],
              [[9,8,7],
               [3,2,1]]])
# print(a.shape)

a = np.arange(100).reshape(5,10,2)
print(a[:,[0,1,4,3]])




























end = time.perf_counter()

print(f"Execution time: {end - start:.6f} seconds")