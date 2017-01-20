# Notes

- [x] 344

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