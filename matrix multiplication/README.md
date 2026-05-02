# Matrix Multiplication using Hadoop MapReduce

---

## 📂 Files

* mapper.py
* reducer.py
* input.txt

---

## 📥 Input File (input.txt)

```
A,0,0,1
A,0,1,2
A,1,0,3
A,1,1,4

B,0,0,5
B,0,1,6
B,1,0,7
B,1,1,8
```

---

## 🧠 Mapper Code (mapper.py)


#!/usr/bin/env python
import sys

N = 2

for line in sys.stdin:
    parts = line.strip().split(',')
    matrix, i, j, val = parts[0], int(parts[1]), int(parts[2]), int(parts[3])

    if matrix == 'A':
        for k in range(N):
            print "%d,%d\tA,%d,%d" % (i, k, j, val)
    else:
        for k in range(N):
            print "%d,%d\tB,%d,%d" % (k, j, i, val)
```

---

## 🧠 Reducer Code (reducer.py)


#!/usr/bin/env python
import sys

current_key = None
values = []

def process(key, values):
    A = {}
    B = {}

    for val in values:
        parts = val.split(',')
        if parts[0] == 'A':
            A[int(parts[1])] = int(parts[2])
        else:
            B[int(parts[1])] = int(parts[2])

    result = 0
    for k in A:
        if k in B:
            result += A[k] * B[k]

    print "%s\t%d" % (key, result)

for line in sys.stdin:
    key, val = line.strip().split('\t')

    if key == current_key:
        values.append(val)
    else:
        if current_key:
            process(current_key, values)
        current_key = key
        values = [val]

if current_key:
    process(current_key, values)
```

---

## 🧪 Commands to Execute

### Step 1: Create input file

```
nano input.txt
```

### Step 2: Create mapper and reducer

```
nano mapper.py
nano reducer.py
```

### Step 3: Give permission

```
chmod +x mapper.py reducer.py
```

### Step 4: Upload to HDFS

```
hdfs dfs -mkdir /input
hdfs dfs -put input.txt /input
```

### Step 5: Remove old output

```
hdfs dfs -rm -r /output
```

### Step 6: Run MapReduce

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /input/input.txt \
-output /output \
-mapper mapper.py \
-reducer reducer.py
```

### Step 7: View Output

```
hdfs dfs -cat /output/part-00000
```

---

## 📌 Notes

* Python 2 syntax is used (no brackets in print)
* Matrix size assumed: 2 × 2
* Mapper emits intermediate key-value pairs
* Reducer computes final multiplication result
