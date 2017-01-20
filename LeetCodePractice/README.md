# Notes

- [x] 344
- [x] 278

## 278. First Bad Version

找出最早的錯誤版本

官方提供一個 API : isBadVersion() 幫助你找到有問題的版本

一開始使用最簡單的暴力破解，從尾巴掃到頭，最早的正確的前一個版本。

```Python

for i in range(n , -1, -1):
	if not isBadVersion(i):
		return i+1
```

但是拿到結果

- Runtime Error Message: Line 23: MemoryError
- Last executed input: 2126753390 versions, 1702766719 is the first bad version.

數字太大，不能這樣玩。

那就改用 Binary Search。

## 344. Reverse String

嘗試使用 `Reversed()` 來反轉，使用方式需要搭配 `for loop`

```Python
result = ""
for i in Reversed(s):
	result = result + i
return result
```

使用 string slice 也可以做到類似功能

```Python
result = ""
for i in range(len(s)-1, -1, -1):
	result = result + s[i]
return
```

> range(10, -1, -1) ，指的是從 10 開始，到 0( -1 前)結束每次 -1，也就是 10, 9, 8 ... 2, 1, 0

### 問題：當字串大的時候，效率非常差。

Google 到 [官方文件 Python Speed](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

> 在 String Concatenation 建議使用 `join`

把上述的 `+` 方式改成

```Python
reversedChar = [ i for i in reversed(s)]
reversedString = "".join(reversedChar)
return reversedString
```

### 觀看別人的解法

有更直觀的寫法，直接用 string slice 反轉

`s[::-1]`