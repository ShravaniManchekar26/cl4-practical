# Word Frequency using Hadoop MapReduce

---

## 📂 Files

* mapper.py
* reducer.py
* input.txt

---

## 📥 Input File (input.txt)

```
data science is fun
big data is powerful
data is everywhere
```

---

## 🧠 Mapper Code (mapper.py)

```python
#!/usr/bin/env python
import sys

target = "data"

for line in sys.stdin:
    words = line.lower().split()
    for word in words:
        if word == target:
            print("%s\t1" % word)
```

---

## 🧠 Reducer Code (reducer.py)

```python
#!/usr/bin/env python
import sys

current_word = None
total = 0

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) != 2:
        continue

    word, count = parts
    count = int(count)

    if word == current_word:
        total += count
    else:
        if current_word:
            print("%s\t%d" % (current_word, total))
        current_word = word
        total = count

if current_word:
    print("%s\t%d" % (current_word, total))
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
hdfs dfs -mkdir /input1
hdfs dfs -put input.txt /input1
```

### Step 5: Remove old output

```
hdfs dfs -rm -r /output1
```

### Step 6: Run MapReduce

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /input1 \
-output /output1
```

### Step 7: View Output

```
hdfs dfs -cat /output1/part-00000
```

---

## 📌 Notes

* Make sure Python scripts are executable
* Use Python 3 syntax (`print()`)
* Output will show frequency of word **"data"**
