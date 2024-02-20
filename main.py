def add(a,b):
    return a+b
def print_function(string):
    return f"hibban is not the main function {string}"

print(add(3,5))
print(print_function("hibban"))

# if __name__ == "__main__":
S="abc"
S=list(S)
b=[]
def permute(S,l,r):
    for i in range(l,r+1):
        temp=S[l]
        S[l]=S[l+i]
        S[l+i]=temp
        permute(S,l+1,r)
        temp=S[l]
        S[l]=S[l+i]
        S[l+i]=temp
        b.append(S)
l=0
r=len(S)-1
permute(S,l,r)
print(b)


def permutations(word):
    if len(word)==1:
        return [word]
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    
    return result

print(permutations('abc'))

n1='{:032b}'.format(2)
print(n1)
print(type(n1))