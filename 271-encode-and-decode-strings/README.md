[ Image ]

### [ LeetCode ] 271. Encode and Decode Strings

### 📌 문제 링크

[LeetCode - Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/description/)

### ⚠️ 제약조건

- 0 <= strs.length < 100
- 0 <= strs[i].length < 200
- strs[i] contains any possible characters out of 256 valid ASCII characters.

### 🛠️ 풀이 접근 및 분석

> Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

-   **접근 1**

    - 문제는 상당히 단순하다. 암호화와 복호화 코드를 구현하면 된다. 암호화 함수인 **encode()** 와 복호화 함수인 **decode()** 부분의 리턴 타입 힌트만 봐도 **encode()** 는 여러개의 단어들을 한번에 암호화 하여 단일 문자열로 만들어야하며, **decode()** 는 그 문자열을 다시 되돌리는 역할을 해야만 한다. 여기서 바로 생각이 든 것이 카이사르 암호화이다. 여기서 문자의 길이만큼 ASCII 값에 더하여, 추가된 값을 저장하는 방식으로 치환한 후 특정 문자로 구분하여 만들면 되지 않을까 싶었다. 하지만 아래와 같은 코드를 구현하다 문제를 파악했다. 먼저 제약 조건에서는 

      > **strs[i] contains any possible characters out of 256 valid ASCII characters.**


    - 라는 문장이 존재한다. 여기서 **256** 가지 **ASCII** 값이 모두 적용 가능하려면 단순 구분자의 역할을 해줄 문자의 존재가 정말 어려워진다. 이외에도 단순 ASCII 값에 문자열의 길이를 더하여 치환을 하게 된다면 만약 **ASCII 256** 보다 큰 값이 나오게 된다면 처리에 있어서 예외상황 처리까지 필요로 하게 된다. 사실 후자의 이유보다 전자의 이유가 치명적이라 다른 접근 방식을 생각해야만 했다.

```python
# 접근 1번의 문제 상황 코드 (구분자 문제 / 치환문제)
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs=[]
        for string in strs:
            length = len(string)
            word = []
            for i in range(length):
                word.append(chr(ord(string[i])+length))
            encoded_strs.append("".join(word))

        return ",".join(encoded_strs)
```

-   **접근 2**

    - 구분자를 사용을 해야만 한다고 생각하면 사실 매우 단순하게 해결이 가능하다. 바로 꼬이지 않게만 만들면 된다는 것이다. **문자열길이[구분자]암호화된문자열** 형식으로 저장한다면, 앞에서 순차적으로만 순회하게 한다면, **[구분자]** 부분에 **ASCII** 의 **256개** 의 값중에 하나를 사용하여, 암호화된 문자열에 우연히 구분자가 포함되어 로직이 꼬일것 같은 상황에서도 결국 문자열길이 덕분에 이 문제를 해결될 수 있다. 이러한 형식을 이어붙여 만들게 된다면 접근 1번에서 가장 걱정했던 문제를 해결할 수 있다.


### 📝 추후 개선점

-  **접근 1번** 에서 아스키값의 오버플로우를 걱정했었다. 하지만 파이썬에서는 이러한 상황에서는 확장 아스키로 변환하여 문제를 발생시키지 않는다. 추후 이러한 상황을 마주했을때 이러한 점을 고려하여 문제상황을 해결해야할 것이다.

### 💻 풀이 코드

```python
#풀이 1 (String)
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=[]
        for string in strs:
            length = len(string)
            word = []
            for i in range(length):
                word.append(chr(ord(string[i])+length))
            encoded_str.append(str(length) + "@" + "".join(word))

        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        
        i=0
        while i<len(s):
            j=i
            while s[j]!="@": #시작지점부터 구분자까지 탐색
                j+=1

            length = int(s[i:j]) #길이부분

            i=j+1 #문자열 시작부분
            encoded_str = s[i:i+length] #문자열 부분
            
            word=[]
            for k in range(length):
                word.append(chr(ord(encoded_str[k])-length))
            decoded_strs.append("".join(word))

            i+=length #다음 지점으로 이동

        return decoded_strs
```

### 🤔 고찰

- 생각보다 단순하지만 뭔가 시행착오가 많았던 문제였다. 처음 **decode** 와 **encode** 함수를 마주했을때 이전에 3가지 암호를 썪어서 삼중 문자열 암호화를 하는 프로그램을 만든 적이 있었는데 그 **3가지 암호화 방식** 중에서 하나인 **카이사르 암호** 방식을 적용했다. 하지만 문자열 조작에 있어서 뭔가 하나 둘 실수라고 하면 실수고 잘못된 접근이라고 하면 잘못된 접근인 부분이 상당했기에 문제를 푸는 시간이 생각보다 더 소요되었다고 생각한다. 정말 주의해야겠다..
