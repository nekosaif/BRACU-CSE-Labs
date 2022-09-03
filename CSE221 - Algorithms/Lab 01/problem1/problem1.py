def isPalindrome(word):
    n = len(word)
    if type(word) != str and word != None and len(word) != 0:
        return False
    for i in range(n//2):
        if word[i] != word[n-1-i]:
            return False
    return True


def file_io_operation(inp, out, rec):
    odd_parity = even_parity = palindrome = cnt = 0
    with open(inp, 'r') as f1, open(out, 'w') as f2, open(rec, 'w') as f3:
        for t in f1.read().strip().split('\n'):
            num, word = t.split(' ')
            out_str = f'{num} has'
            
            if not '.' in num:
                if int(num)&1 == 1:
                    odd_parity += 1
                    out_str += f' odd parity and {word} is'
                else:
                    even_parity += 1
                    out_str += f' even parity and {word} is'
            else:
                 out_str += f' cannot have parity and {word} is'
            
            if isPalindrome(word):
                out_str += f' a palindrome'
                palindrome += 1
            else:
                out_str += f' not a palindrome'
            
            f2.write(out_str + '\n')
            cnt += 1
        else:
            out_str = f'''Percentage of odd parity: {odd_parity/cnt*100}%
Percentage of even parity: {even_parity/cnt*100}%
Percentage of no parity: {(cnt-odd_parity-even_parity)/cnt*100}%
Percentage of palindrome: {palindrome/cnt*100}%
Percentage of non-palindrome: {(cnt-palindrome)/cnt*100}%'''
            f3.write(out_str)
        
             
        

def main():
    file_io_operation('input.txt', 'output.txt', 'record.txt')


if __name__ == '__main__':
    main()