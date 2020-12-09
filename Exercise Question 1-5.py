#!/usr/bin/env python
# coding: utf-8

# Execise Question Homework

# Patcharapong  Sutiyut 6310301026

# # Q.1

# In[2]:


ListA =  [3,6,9,12,15,18,21]
ListB =  [4,8,12,16,20,24,28]
ListC,ListD,ListE = [],[],[]
print("Element at odd-index position from list one")
for i in range(1,len(ListA)):
    if i % 2 == 0 :
        ListD.append(ListA[i-1])
print(ListD)
    
print("Element a even-index position from list two")
for i in range(1,len(ListB)+1):
    if i % 2 != 0 :
        ListE.append(ListB[i-1])
print(ListE)

print("Printing final thord list ")
ListC = [i for i in ListD]
ListC += [ i for i in ListE]
print(ListC)


# # Q.2

# In[7]:


ListT = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", ListT)
element = ListT.pop(4)
print("List After removing element at index 4 ", ListT)

ListT.insert(2, element)
print("List after Adding element at index 2 ", ListT)

ListT.append(element)
print("List after Adding element at last ", ListT)


# # Q.3

# In[6]:


ListM = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sampleList)

length = len(ListM)
chunkSize  = int(length/3)
start = 0
end = chunkSize
for i in range(1, 4, 1):
  indexes = slice(start, end, 1)
  listChunk = ListM[indexes]
  print("Chunk ", i , listChunk)
  print("After reversing it ", list(reversed(listChunk)))
  start = end
  if(i != 2):
    end +=chunkSize
  else:
    end += length - chunkSize


# # Q.4

# In[8]:


ListH = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", ListH)

countDict = dict()
for item in ListH:
    if(item in countDict):
        countDict[item] += 1
    else:
        countDict[item] = 1
print("Printing count of each item  ",countDict)


# # Q.5

# In[9]:


first = [2,3,4,5,6,7,8]
second = [4,9,16,25,36,49,64]
result = set()
for i in first :
    if (i*i) in second :
        result.add(tuple([i,second[second.index(i*i)]]))
print("First List",first)
print("second",second)
print("Result is",result)

