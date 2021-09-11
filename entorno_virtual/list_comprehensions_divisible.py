def run():
    # squarse = []
    # for i in range(1,1000):
    #     if(i**2)%3 ==0:
    #         continue
    #     else:
    #         squarse.append(i**2)
    squarse =[i**2 for i in range(1,101) if i%3 !=0 ]
    print(squarse)

if __name__=='__main__':
    run()