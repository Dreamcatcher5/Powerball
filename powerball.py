max_white = 69
whiteList = {}
for i in range(1,max_white+1):
    whiteList[i] = 0.0;
lrp = {}
for i in range(1,max_white+1):
    lrp[i] = 0;
wc = 0
max_red = 26
redList = {}
for i in range(1,max_red+1):
    redList[i] = 0.0;
rc = 0
lrpr = {}
for i in range(1,max_red+1):
    lrpr[i] = 0;
iw = 1
ir = 1
f = open("powerball.txt")
for line in f:
    balls = line.split()
    #print balls
    # Do whites
    for b in range(1,6):
        whiteList[int(balls[b])] += 1
        wc += 1
        if lrp[int(balls[b])] == 0:
            lrp[int(balls[b])] = iw # balls with highest i are last recently picked
        iw += 1
    # Do red ball
    if  not int(balls[6]) > max_red:
        redList[int(balls[6])] += 1
        if lrpr[int(balls[6])] == 0:
            lrpr[int(balls[6])] = ir # balls with highest i are last recently picked
        ir += 1
        rc += 1

# Compile everything, print results
white_sorted = whiteList.keys()
for i in range(60,70):
    whiteList[i] *= 63.3
white_sorted.sort(cmp=lambda x,y: cmp(whiteList[x], whiteList[y]))
print
print "White Balls:"
for i in white_sorted:
    print "Ball %d: %f" % (i, whiteList[i]*100/wc)
    
white_sorted = lrp.keys()
white_sorted.sort(cmp=lambda x,y: -1*cmp(lrp[x], lrp[y]))
print
print "Least Recent White Balls:"
for i in white_sorted:
    print "Ball %d: %f" % (i, lrp[i])

#Red balls
red_sorted = redList.keys()

red_sorted.sort(cmp=lambda x,y: -cmp(redList[x], redList[y]))
print
print "Red Balls:"
for i in red_sorted:
    print "Ball %d: %f" % (i, redList[i]*100/rc)
    

red_sorted = lrpr.keys()
red_sorted.sort(cmp=lambda x,y: -1*cmp(lrpr[x], lrpr[y]))
print
print "Least Recent Red Balls:"
for i in red_sorted:
    print "Ball %d: %f" % (i, lrpr[i])


