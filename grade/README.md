# Matrix Multiplication using Hadoop MapReduce

---

## 📂 Files

* mapper.py
* reducer.py
* input.txt

---

## 📥 Input File (input.txt)

```
101,Math,95
101,English,88
102,Math,72
102,Science,68
103,Math,55

```

---

## 🧠 Mapper Code (mapper.py)
#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    parts = line.split(",")
    if len(parts) != 3:
        continue

    student_id, subject, marks = parts

    try:
        marks = float(marks)
        print "%s\t%s" % (student_id, marks)
    except:
        continue

```

---

## 🧠 Reducer Code (reducer.py)

#!/usr/bin/env python
import sys

current_student = None
marks_list = []

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

for line in sys.stdin:
    line = line.strip()
    student_id, marks = line.split("\t")
    marks = float(marks)

    if current_student == student_id:
        marks_list.append(marks)
    else:
        if current_student:
            avg = sum(marks_list) / len(marks_list)
            grade = calculate_grade(avg)
            print "%s,%0.2f,%s" % (current_student, avg, grade)

        current_student = student_id
        marks_list = [marks]

if current_student:
    avg = sum(marks_list) / len(marks_list)
    grade = calculate_grade(avg)
    print "%s,%0.2f,%s" % (current_student, avg, grade)


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
