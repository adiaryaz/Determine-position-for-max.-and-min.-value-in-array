# Determine position for max. and min. value in array

A program to find the index positions of the first occurrences of the maximum and minimum values within a 1-dimensional array (list) of integers.

## 📝 Description

This program analyzes a given list of numbers to identify the largest and smallest values. It then returns the index (position) where these values are first found. The program must also validate that the input list contains *only* integer values.

-----

## 🎯 Problem Statement

### Input:

  * A single line representing a list of numbers (e.g., `[1, 2, 3]`).

### Output:

  * The index of the minimum value and the index of the maximum value, separated by a comma: `min_position, max_position`.
  * **"Not Array, it is List."** if the input list contains any non-integer elements.

### Rules:

1.  The program must find the **position (index)**, not the value itself.
2.  If the minimum or maximum value appears multiple times, the index of the **first occurrence** is used.
3.  If the list contains only one element, the minimum and maximum position are both `0`.
4.  The list must *only* contain integers. If any element is not an integer (e.g., a string), the program must output the specified error message.
5.  Array indices start at `0`.

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
[1, 4, 5, 10, 2]
```

**Output:**

```
0, 3
```

**Explanation:** The minimum value is `1` (at index 0). The maximum value is `10` (at index 3).

### Example 2 (Sample 2)

**Input:**

```
[10, 2, 0, 5, 15, 16]
```

**Output:**

```
2, 5
```

**Explanation:** The minimum value is `0` (at index 2). The maximum value is `16` (at index 5).

### Example 3 (Sample 3)

**Input:**

```
[10, 20, 34, 20, 30]
```

**Output:**

```
0, 2
```

**Explanation:** The minimum value is `10` (at index 0). The maximum value is `34` (at index 2).

### Example 4 (Sample 4)

**Input:**

```
[10]
```

**Output:**

```
0, 0
```

**Explanation:** The minimum and maximum value is `10` (at index 0).

### Example 5 (Sample 5)

**Input:**

```
[1, 3, 4, "test", 2]
```

**Output:**

```
Not Array, it is List.
```

**Explanation:** The input list contains a non-integer (a string "test").

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiayaz/array-minmax-position.git
    cd array-minmax-position
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Enter the array in list format (e.g., `[1, 4, 5, 10, 2]`) when prompted to see the result.
