# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 08:54:44 2022

@author: USER
"""
# # Inefficient:, time limit exceeded when processing large input
# See suggested solution when reviewing it later
# Self note:  using dict would be good enough


# Problem Description
 
# You are given a 2D string array A of dimensions N x 2,

# where each row consists of two strings: first is the name of the student, second is their marks.

# You have to find the maximum average mark. If it is a floating point, round it 
# down to the nearest integer less than or equal to the number.

# Problem Constraints
# 1 <= N <= 105

# Input Format
# The first argument is a 2D string array A.

# Output Format
# Return a single integer which is the highest average mark.

# Example Input
# Input 1:
A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"]]
# Input 2:
A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"], ["Alice", "10"]]

# Example Output
# Output 1:90
# Output 2:85

# Example Explanation
# Explanation 1:
# Alice has the highest average with 90 marks.
# Explanation 2:

# Bob has the highest average with 85 marks.
# class Solution:
#     # @param A : list of list of strings
#     # @return an integer
#     def highestScore(self, A):
    


def highestScore(A):
    import math
    buckets = []
    numBuckets = 26
    # len_A = len(A)
    
    for i in range(numBuckets):
        buckets.append([])
    
    def processRow(name, mark):
        # name = str(name)
        firstLet = (ord(name[0])- 65) % 26
        hashBuck = buckets[firstLet]
        # print(hashBuck, firstLet)
        isHashed = False
        for i in range(len(hashBuck)):
            # print('start')
            if hashBuck[i][0] == name:
                # print('there')
                isHashed = True
                hashBuck[i][1].append(mark)
                hashBuck[i][2] += 1
                # hashBuck[i][3] = math.floor(sum(hashBuck[i][1]) / hashBuck[i][2])
                break
            # else:
                # print('here')
        if not(isHashed):
            hashBuck.append([name, [mark], 1, mark])
        # print(hashBuck)
        
    for i in A:
        # print(i, i[0], i[1])
        processRow(str(i[0]), int(i[1]))
    
    # print(buckets)
    cur_max = 0
    # cur_name = 'NA'
    for j in range(len(buckets)):
        # print(j)
        for k in range(len(buckets[j])):
            # print(buckets[j][k][1], buckets[j][k][2])
            buckets[j][k].append(math.floor(sum(buckets[j][k][1]) / buckets[j][k][2] ))
            # print( buckets[j][k] )
            if buckets[j][k][4] > cur_max:
                cur_max = buckets[j][k][4]
    return cur_max
highestScore(A)



# Suggested Solution:
# from collections import defaultdict
# class Solution:
#     # @param A : list of list of strings
#     # @return an integer
#     def highestScore(self, A):
#         dic=defaultdict(list)
#         for val in A:
#             dic[val[0]].append(int(val[1]))
        
#         ans=0
#         for val in dic.values():
#             n=len(val)
#             tot=sum(val)
#             avg=tot//n
#             ans=max(ans,avg)
#         return ans
# C++
# int Solution::highestScore(vector < vector < string > > & A) {
#     map < string, pair < int, int >> mp;
#     for (int i = 0; i < A.size(); i++) {
#         if (mp.find(A[i][0]) == mp.end()) {
#             mp[A[i][0]] = make_pair(0, 0);
#         }
#         mp[A[i][0]] = make_pair(mp[A[i][0]].first + stoi(A[i][1]), mp[A[i][0]].second + 1);
#     }
#     int ans = 0;
#     for (auto & x: mp) {
#         ans = max(ans, x.second.first / x.second.second);
#     }
#     return ans;
# }
# /**
#  * @input A : 2D string array
#  * 
#  * @Output Integer
#  */
# import "strconv"
# //import "fmt"

# func highestScore(A [][]string )  (int) {
#     avgMarks := make(map[string]int)
#     timesSeen := make(map[string]int)

#     for i := 0; i < len(A); i++ {
#         curName := A[i][0]
#         _, found := avgMarks[curName]
#         if !found {
#             avgMarks[curName], _ = strconv.Atoi(A[i][1])
#             timesSeen[curName] = 1
#             continue
#         }
        
#         curMark, _ := strconv.Atoi(A[i][1])
#         avgMarks[curName] += curMark
#         timesSeen[curName] ++
#     }

#     //fmt.Println(avgMarks)
#     //fmt.Println(timesSeen)

#     for key, _ := range avgMarks {
#         avgMarks[key] = avgMarks[key] / timesSeen[key]
#     }

#     highest := -1
#     for _, value := range avgMarks {
#         if value > highest {highest = value}
#     }

#     return highest
# }






# A = [  [wwev, 40],
#   [exqe, 44],
#   [xmx, 38],
#   [hkf, 45],
#   [kjm, 54],
#   [sndup, 63],
#   [awoc, 25],
#   [krgb, 25],
#   [vkgf, 69],
#   [vub, 99],
#   [gadvp, 63],
#   [shbv, 97],
#   [rnauu, 42],
#   [ikcwf, 41],
#   [wjv, 28],
#   [dztmy, 85],
#   [nrc, 11],
#   [efcb, 72],
#   [nycp, 56],
#   [newb, 48],
#   [enyci, 72],
#   [wqd, 21],
#   [twmh, 61],
#   [icils, 21],
#   [qjlwc, 10],
#   [mkwkz, 3],
#   [dcc, 35],
#   [xark, 76],
#   [lflwk, 30],
#   [arxrq, 72],
#   [ewn, 54],
#   [tlm, 10],
#   [udyq, 70],
#   [zgf, 23],
#   [sshi, 4],
#   [akk, 36],
#   [eohet, 12],
#   [xzaij, 64],
#   [ngdkq, 39],
#   [ijqpg, 60],
#   [mwz, 17],
#   [kivo, 70],
#   [stczw, 19],
#   [psuoc, 49],
#   [lerjb, 47],
#   [aley, 23],
#   [rvwq, 29],
#   [sslys, 54],
#   [lux, 18],
#   [wlybn, 30],
#   [ukie, 12],
#   [vkew, 88],
#   [pean, 38],
#   [gqqi, 91],
#   [stjke, 68],
#   [scbm, 3],
#   [xpi, 43],
#   [wtmn, 22],
#   [nzy, 25],
#   [rvcgh, 8],
#   [rucuq, 75],
#   [xchba, 49],
#   [pll, 24],
#   [yigt, 2],
#   [zjoak, 71],
#   [btuzj, 21],
#   [yll, 34],
#   [mbobi, 96],
#   [oppu, 65],
#   [vimrp, 28],
#   [kzg, 6],
#   [lljzx, 68],
#   [spuu, 39],
#   [ztan, 65],
#   [xvv, 59],
#   [hlxxp, 42],
#   [yfvf, 62],
#   [qhhh, 61],
#   [stpy, 7],
#   [nzl, 45],
#   [bviqd, 23],
#   [xtyxu, 43],
#   [tye, 8],
#   [shv, 20],
#   [ybn, 2],
#   [wgadv, 85],
#   [ibde, 22],
#   [emnv, 82],
#   [aixzn, 61],
#   [fmqk, 29],
#   [tlr, 7],
#   [zljz, 94],
#   [odbv, 5],
#   [mzlgy, 72],
#   [lik, 74],
#   [lqqc, 31],
#   [ifmc, 65],
#   [ketc, 5],
#   [djpxx, 64],
#   [mpl, 65],
#   [czk, 0],
#   [kaho, 27],
#   [kku, 49],
#   [htiu, 37],
#   [axqp, 11],
#   [iru, 22],
#   [xtvr, 83],
#   [fui, 56],
#   [hxuhm, 19],
#   [ighyp, 74],
#   [thrfa, 97],
#   [dzsv, 52],
#   [vhcsu, 99],
#   [fgq, 12],
#   [zyooa, 48],
#   [mfp, 1],
#   [dus, 56],
#   [ouvuo, 29],
#   [eptmz, 73],
#   [pcok, 78],
#   [ryyqk, 30],
#   [rzwbt, 78],
#   [xfaur, 33],
#   [wytp, 49],
#   [zjywz, 85],
#   [xrri, 38],
#   [cocek, 64],
#   [lwxc, 69],
#   [cpudt, 9],
#   [pean, 81],
#   [xmf, 10],
#   [vlnv, 79],
#   [wztyo, 33],
#   [vpm, 33],
#   [uczzw, 36],
#   [pafe, 95],
#   [pnri, 68],
#   [mjxqn, 31],
#   [uotx, 91],
#   [gjx, 60],
#   [hgno, 63],
#   [wgomr, 62],
#   [dxpz, 19],
#   [kgr, 73],
#   [wnzbp, 92],
#   [eoqp, 67],
#   [piwkr, 80],
#   [gsfm, 88],
#   [txdv, 92],
#   [cwxt, 33],
#   [gmuct, 28],
#   [cdmu, 79],
#   [xrvvb, 69],
#   [jkskl, 82],
#   [sfh, 23],
#   [hfi, 25],
#   [zrhew, 20],
#   [jjdmv, 88],
#   [tfx, 58],
#   [igip, 68],
#   [mjfr, 0],
#   [yimx, 49],
#   [wvg, 28],
#   [eig, 42],
#   [xrt, 32],
#   [luezu, 74],
#   [ajeke, 31],
#   [zsn, 83],
#   [zwb, 17],
#   [bvrrm, 79],
#   [xvm, 63],
#   [ympzj, 88],
#   [moyn, 12],
#   [kanj, 57],
#   [hhnh, 81],
#   [fthb, 55],
#   [useca, 56],
#   [pxmvx, 70],
#   [evpld, 53],
#   [ujlc, 76],
#   [hlwna, 94],
#   [ybxa, 84],
#   [nyrnj, 95],
#   [gzfq, 37],
#   [nhly, 58],
#   [maooa, 78],
#   [chywv, 10],
#   [ycfx, 86],
#   [fyaqd, 56],
#   [keyg, 84],
#   [iggdv, 36],
#   [xskwr, 41],
#   [etw, 25],
#   [qaeif, 7],
#   [ijoff, 62],
#   [cwko, 66],
#   [zkdn, 25],
#   [kksyt, 98],
#   [ihy, 46],
#   [akucz, 52],
#   [haen, 39],
#   [hlecm, 66],
#   [khaig, 91],
#   [jygy, 53],
#   [qrij, 0],
#   [sxrjj, 87],
#   [lihqg, 71],
#   [lyv, 82],
#   [idklk, 86],
#   [mnodx, 88],
#   [bwnj, 33],
#   [xxrg, 49],
#   [hvt, 2],
#   [gbuyu, 30],
#   [xqu, 99],
#   [odqk, 16],
#   [gci, 6],
#   [ksv, 80],
#   [fam, 72],
#   [udunf, 72],
#   [lpxa, 43],
#   [mluj, 68],
#   [vin, 86],
#   [ochop, 70],
#   [vyqn, 55],
#   [wxzp, 84],
#   [hnms, 89],
#   [kefxs, 79],
#   [dptwl, 16],
#   [jmv, 42],
#   [rfbs, 41],
#   [njjk, 13],
#   [qih, 79],
#   [qjg, 84],
#   [dphxd, 92],
#   [qvis, 36],
#   [yhsbn, 6],
#   [qxskw, 56],
#   [iyd, 89],
#   [ycgd, 42],
#   [fhlx, 82],
#   [rgxq, 57],
#   [pzc, 90],
#   [uowmu, 34],
#   [biw, 24],
#   [iyazz, 99],
#   [gzii, 38],
#   [imfcq, 52],
#   [fbhlu, 87],
#   [iape, 34],
#   [zpiwm, 15],
#   [tstz, 3],
#   [dozk, 8],
#   [wjxnq, 3],
#   [kxhaz, 48],
#   [guju, 77],
#   [jwexu, 60],
#   [trr, 65],
#   [scxc, 32],
#   [qrphi, 46],
#   [plxe, 6],
#   [tvt, 25],
#   [csfep, 21],
#   [nfgno, 24],
#   [ykq, 30],
#   [vkohi, 49],
#   [lak, 17],
#   [wczkp, 16],
#   [hldi, 66],
#   [zhy, 84],
#   [bwwp, 7],
#   [tudbt, 43],
#   [uhase, 59],
#   [wnam, 97],
#   [yupv, 90],
#   [bwgnc, 38],
#   [vaa, 77],
#   [gcwrs, 95],
#   [beesg, 81],
#   [qre, 82],
#   [yagl, 87],
#   [pmg, 87],
#   [mpe, 70],
#   [ciao, 59]
#   [ndap, 31],
#   [iwyn, 65],
#   [qrimr, 31],
#   [pdyfb, 97],
#   [ygrvy, 79],
#   [vqyg, 52],
#   [ujr, 34],
#   [lbpyb, 94],
#   [zdal, 29],
#   [eccxh, 38],
#   [fpzih, 4],
#   [nolzs, 0],
#   [mmeb, 30],
#   [edol, 66],
#   [wzpkm, 77],
#   [waudc, 49],
#   [eej, 84],
#   [wbk, 60],
#   [nxogl, 34],
#   [siggw, 5],
#   [qjv, 40],
#   [veunt, 92],
#   [qqu, 47],
#   [pxkrc, 22],
#   [fcan, 15],
#   [gjfcy, 10],
#   [nxa, 61],
#   [mqrh, 80],
#   [cxr, 8],
#   [vlgq, 75],
#   [zhr, 92],
#   [kyri, 29],
#   [ntgdl, 60],
#   [tbffw, 6],
#   [rryn, 29],
#   [uof, 17],
#   [wblrr, 8],
#   [zpz, 7],
#   [kyv, 53],
#   [xkaqk, 6],
#   [hrcl, 11],
#   [rghkd, 23],
#   [vdiux, 88],
#   [uncbh, 69],
#   [bqrzo, 93],
#   [wsao, 17],
#   [mtld, 46],
#   [wjsad, 23],
#   [dww, 60],
#   [vti, 51],
#   [oeuln, 1],
#   [gzcs, 1],
#   [yxb, 86],
#   [yly, 82],
#   [vgo, 0],
#   [mke, 55],
#   [npq, 12],
#   [swkg, 81],
#   [tyo, 17],
#   [hoi, 8],
#   [gqc, 48],
#   [lls, 58],
#   [xnw, 7],
#   [fqu, 95],
#   [ijv, 4],
#   [brdou, 22],
#   [jyo, 16],
#   [lfu, 87],
#   [tflab, 4],
#   [zbfxp, 45],
#   [rap, 48],
#   [fbw, 28],
#   [ttfyn, 27],
#   [xso, 79],
#   [png, 11],
#   [nzzl, 84],
#   [pjw, 66],
#   [fho, 72],
#   [geape, 51],
#   [zdhxc, 54],
#   [kajjl, 43],
#   [jxjmw, 89],
#   [tza, 95],
#   [xzrj, 21],
#   [zzpy, 10],
#   [nkli, 12],
#   [xbhcx, 81],
#   [pag, 26],
#   [mxg, 51],
#   [oyo, 82],
#   [ioce, 36],
#   [duuq, 29],
#   [tbk, 74],
#   [xqrxj, 88],
#   [hfi, 62],
#   [sep, 15],
#   [rhum, 17],
#   [qico, 42],
#   [fbk, 83],
#   [zvpql, 79],
#   [qpg, 85],
#   [iqm, 98],
#   [ril, 59],
#   [tgt, 35],
#   [cfkvp, 77],
#   [ulpm, 14],
#   [tkqm, 75],
#   [xuqe, 23],
#   [edyww, 89],
#   [ykzx, 42],
#   [olywr, 93],
#   [qkfu, 14],
#   [fxt, 15],
#   [qhfex, 9],
#   [tau, 18],
#   [knvog, 39],
#   [unbi, 37],
#   [lehre, 4],
#   [vqo, 78],
#   [ngrpq, 13],
#   [lkm, 36],
#   [lcdo, 15],
#   [wsju, 24],
#   [ocgf, 83],
#   [qqpdw, 26],
#   [nxkv, 21],
#   [kttog, 6],
#   [vdb, 84],
#   [paa, 25],
#   [uem, 16],
#   [pzif, 10],
#   [vgh, 19],
#   [qyw, 21],
#   [vmaee, 90],
#   [fmkt, 11],
#   [xgkt, 11],
#   [fxs, 81],
#   [ahty, 33],
#   [vlhts, 87],
#   [mxdbf, 44],
#   [fxd, 30],
#   [wjukq, 15],
#   [jovcf, 26],
#   [pmqb, 12],
#   [hsqsv, 82],
#   [lsnz, 98],
#   [bces, 57],
#   [rtaj, 58],
#   [kdpf, 45],
#   [vce, 40],
#   [hcy, 24],
#   [wkw, 30],
#   [mipy, 63],
#   [lrq, 59],
#   [vvx, 52],
#   [dubxc, 70],
#   [bfdr, 20],
#   [gfnuf, 58]
#   # [jwfv, 21],
#   # [kkbzs, 34]
#   # [ucltf, 82]
#   # [biyvn, 82]
#   # [vjano, 33]
#   # [hrqhx, 28]
#   # [ndsri, 6]
#   # [wqj, 17]
#   # [vxxsb, 78]
#   # [voqoj, 41]
#   # [wcuf, 71]
#   # [giaig, 6]
#   # [ukfk, 12]
#   # [rjeih, 13]
#   # [dfbxf, 9]
#   # [iqszi, 83]
#   # [wat, 47]
#   # [ilnjy, 94]
#   # [lkbjg, 78]
#   # [hguu, 61]
#   # [ywh, 57]
#   # [sksu, 42]
#   # [vyc, 52]
#   # [jwlbf, 95]
#   # [pucll, 73]
#   # [grhx, 64]
#   # [bmlsb, 89]
#   # [eru, 94]
#   # [dgce, 65]
#   # [veh, 62]
#   # [hisz, 76]
#   # [oxa, 26]
#   # [fckzz, 68]
#   # [ohm, 37]
#   # [tvnek, 22]
#   # [yebay, 86]
#   # [epc, 32]
#   # [paj, 75]
#   # [tocc, 18]
#   # [zjoak, 96]
#   # [bbd, 53]
#   # [lej, 19]
#   # [tdzpt, 7]
#   # [mjoj, 99]
#   # [nqr, 28]
#   # [bou, 64]
#   # [mrd, 26]
#   # [msdu, 6]
#   # [buw, 97]
#   # [shikd, 94]
#   # [ssb, 25]
#   # [cpe, 55]
#   # [wer, 72]
#   # [ifgr, 91]
#   # [brib, 17]
#   # [ikwau, 97]
#   # [djbro, 31]
#   # [msyi, 43]
#   # [zxze, 0]
#   # [foh, 84]
#   # [alqg, 5]
#   # [kuwfe, 3]
#   # [aibn, 47]
#   # [vpbz, 0]
#   # [aqcoq, 0]
#   # [wfsx, 61]
#   # [bgaf, 44]
#   # [nri, 66]
#   # [rsthc, 32]
#   # [dhae, 42]
#   # [pdmlg, 72]
#   # [frdi, 33]
#   # [kamdm, 41]
#   # [ozajr, 15]
#   # [jrszz, 58]
#   # [tjkp, 94]
#   # [uujb, 72]
#   # [pbvql, 72]
#   # [fkv, 98]
#   # [xlbih, 68]
#   # [hfi, 78]
#   # [hqlv, 7]
#   # [ura, 78]
#   # [dng, 72]
#   # [vbew, 7]
#   # [lyxeh, 5]
#   # [qnm, 16]
#   # [kps, 90]
#   # [wyhk, 48]
#   # [udqz, 7]
#   # [gwr, 41]
#   # [zgjpu, 65]
#   # [ceoq, 89]
#   # [hkr, 94]
#   # [naeh, 11]
#   # [pel, 18]
#   # [rxsvn, 28]
#   # [kphng, 3]
#   # [aeiwy, 24]
#   # [ibmu, 93]
#   # [widi, 59]
#   # [csmqk, 55]
#   # [ejkc, 48]
#   # [rqjy, 86]
#   # [knmr, 57]
#   # [noicm, 47]
#   # [plix, 82]
#   # [ktel, 57]
#   # [qnqv, 57]
#   # [nqjot, 33]
#   # [btq, 59]
#   # [exlpg, 2]
#   # [pirlb, 88]
#   # [jusgd, 77]
#   # [nffu, 97]
#   # [jbffp, 41]
#   # [avtlk, 55]
#   # [teke, 20]
#   # [fdl, 73]
#   # [jzur, 22]
#   # [wlqx, 30]
#   # [cjre, 48]
#   # [cohoc, 13]
#   # [lrflo, 6]
#   # [fptg, 58]
#   # [hikm, 73]
#   # [uxhje, 90]
#   # [ljog, 11]
#   # [phzm, 60]
#   # [ojqe, 73]
#   # [zwbu, 94]
#   # [pao, 87]
#   # [phi, 63]
#   # [xgk, 73]
#   # [dxz, 30]
#   # [msht, 6]
#   # [kqch, 33]
#   # [juinr, 41]
#   # [fdvjs, 37]
#   # [bwg, 39]
#   # [xsba, 89]
#   # [nmq, 7]
#   # [umfc, 35]
#   # [nhg, 82]
#   # [oddxf, 46]
#   # [wyym, 40]
#   # [zktq, 19]
#   # [ueczm, 1]
#   # [fdw, 50]
#   # [bbqjr, 57]
#   # [mdros, 92]
#   # [ita, 73]
#   # [epw, 0]
#   # [ksdr, 54]
#   # [afegu, 27]
#   # [vzpgi, 21]
#   # [hmu, 35]
#   # [xzaij, 22]
#   # [fnz, 67]
#   # [ykji, 99]
#   # [ubha, 48]
#   # [cgutq, 57]
#   # [rlepo, 74]
#   # [ygwkt, 37]
#   # [ktzy, 14]
#   # [vtgzd, 44]
#   # [yrzne, 3]
#   # [gwd, 37]
#   # [mpngr, 53]
#   # [tnu, 20]
#   # [xej, 30]
#   # [nlbz, 4]
#   # [lwa, 26]
#   # [xcc, 26]
#   # [qoo, 5]
#   # [arcq, 30]
#   # [ggq, 8]
#   # [zjmxi, 28]
#   # [jey, 2]
#   # [msbpi, 23]
#   # [ddz, 38]
#   # [vmrc, 30]
#   # [lfd, 30]
#   # [wnl, 24]
#   # [nml, 82]
#   # [oqe, 26]
#   # [ohk, 27]
#   # [myg, 8]
#   # [xoj, 44]
#   # [tebb, 28]
#   # [xydl, 10]
#   # [qvo, 98]
#   # [twrp, 96]
#   # [fnk, 17]
#   # [wnohq, 65]
#   # [uogt, 29]
#   # [zqv, 86]
#   # [hkq, 68]
#   # [pania, 65]
#   # [xst, 19]
#   # [tntxb, 33]
#   # [ifrdz, 24]
#   # [cemq, 61]
#   # [lyfe, 16]
#   # [xfowh, 3]
#   # [wzlsi, 11]
#   # [nedq, 9]
#   # [qur, 65]
#   # [qzdy, 34]
#   # [bimre, 97]
#   # [vehnk, 83]
#   # [yhfwi, 5]
#   # [snry, 58]
#   # [bvss, 21]
#   # [lwp, 45]
#   # [iwze, 13]
#   # [wqj, 0]
#   # [fbkom, 94]
#   # [ukspi, 21]
#   # [umk, 37]
#   # [ujr, 88]
#   # [qzu, 55]
#   # [vmd, 83]
#   # [swph, 45]
#   # [cfft, 80]
#   # [sjioo, 35]
#   # [dpmgw, 17]
#   # [ewvp, 57]
#   # [eup, 30]
#   # [gyse, 73]
#   # [ume, 50]
#   # [fynbf, 20]
#   # [cjk, 77]
#   # [yikol, 49]
#   # [bsgr, 94]
#   # [xrsqg, 39]
#   # [rctvg, 20]
#   # [jfwf, 56]
#   # [ghz, 35]
#   # [bquhf, 43]
#   # [kfq, 53]
#   # [cjq, 56]
#   # [cjq, 43]
#   # [vmxrx, 62]
#   # [lgk, 22]
#   # [vkjm, 9]
#   # [gcxss, 91]
#   # [bvkea, 66]
#   # [slpp, 27]
#   # [jym, 16]
#   # [ctgst, 21]
#   # [yzk, 6]
#   # [axcf, 58]
#   # [nebi, 39]
#   # [kxuzg, 98]
#   # [sxdu, 70]
#   # [kiay, 40]
#   # [pvqp, 34]
#   # [mhg, 96]
#   # [dqjjn, 11]
#   # [qmyxj, 42]
#   # [jnff, 20]
#   # [mpq, 16]
#   # [aht, 68]
#   # [xag, 85]
#   # [zxnf, 31]
#   # [gusjr, 69]
#   # [mqqa, 50]
#   # [vwnbi, 1]
#   # [qxciq, 23]
#   # [zfvwk, 95]
#   # [wjm, 88]
#   # [daai, 19]
#   # [ozqgi, 11]
#   # [ebyhg, 33]
#   # [gxgr, 63]
#   # [qyawy, 46]
#   # [cntx, 22]
#   # [epq, 58]
#   # [sgnle, 98]
#   # [kax, 53]
#   # [pdmgv, 11]
#   # [uzx, 7]
#   # [npqb, 10]
#   # [aerk, 75]
#   # [umt, 80]
#   # [inyz, 83]
#   # [sdiy, 7]
#   # [bueqc, 65]
#   # [vhl, 42]
#   # [usgwi, 21]
#   # [lgy, 69]
#   # [acs, 47]
#   # [pnxhh, 35]
#   # [jvwbp, 49]
#   # [aomcy, 43]
#   # [bczof, 26]
#   # [vvw, 59]
#   # [cbwj, 10]
#   # [tom, 7]
#   # [hfj, 2]
#   # [cet, 95]
#   # [bja, 45]
#   # [sez, 96]
#   # [jzxwr, 53]
#   # [neokz, 76]
#   # [azk, 13]
#   # [kph, 38]
#   # [yrvrt, 31]
#   # [vhyvt, 52]
#   # [abc, 76]
#   # [bkfi, 53]
#   # [scbf, 80]
#   # [nprn, 83]
#   # [bzd, 47]
#   # [xpk, 25]
#   # [xxvi, 20]
#   # [jtsiv, 63]
#   # [pld, 22]
#   # [jur, 83]
#   # [tqse, 61]
#   # [rgp, 4]
#   # [qwn, 64]
#   # [sqtgz, 18]
#   # [hgwyj, 55]
#   # [uycz, 96]
#   # [ssr, 12]
#   # [mws, 54]
#   # [alsg, 83]
#   # [uoplz, 79]
#   # [rina, 6]
#   # [hfd, 0]
#   # [hvax, 88]
#   # [iqzzt, 48]
#   # [sgtqn, 82]
#   # [krs, 51]
#   # [qnyuo, 16]
#   # [dhcas, 98]
#   # [yeth, 14]
#   # [ccaqz, 28]
#   # [fou, 27]
#   # [gia, 63]
#   # [ialto, 80]
#   # [sev, 83]
#   # [xhdg, 94]
#   # [msos, 36]
#   # [vwbxf, 18]
#   # [bdxaq, 95]
#   # [nzx, 18]
#   # [wma, 74]
#   # [uewb, 96]
#   # [cfiv, 49]
#   # [lkyq, 26]
#   # [nmsy, 10]
#   # [fepu, 57]
#   # [gqgs, 54]
#   # [wut, 11]
#   # [chbzc, 94]
#   # [btnz, 85]
#   # [qriw, 88]
#   # [bkb, 95]
#   # [fbjo, 93]
#   # [ucpt, 43]
#   # [bxs, 84]
#   # [aqie, 21]
#   # [nbklh, 82]
#   # [kukuf, 36]
#   # [uhsk, 94]
#   # [bebao, 79]
#   # [bziuk, 29]
#   # [xgvsg, 3]
#   # [foik, 42]
#   # [dxtl, 52]
#   # [qtrfy, 39]
#   # [rmvfm, 94]
#   # [twi, 72]
#   # [qml, 45]
#   # [ogv, 22]
#   # [dyi, 15]
#   # [kke, 49]
#   # [doig, 23]
#   # [ugwff, 3]
#   # [wnlgp, 92]
#   # [xdwr, 67]
#   # [mcmea, 19]
#   # [bnjm, 30]
#   # [jdodn, 64]
#   # [exb, 97]
#   # [yuofp, 32]
#   # [smwpc, 40]
#   # [tyc, 36]
#   # [yljq, 68]
#   # [lpab, 28]
#   # [xzvfk, 84]
#   # [hjhh, 7]
#   # [dboti, 7]
#   # [teab, 71]
#   # [bnb, 17]
#   # [iij, 97]
#   # [fbpe, 71]
#   # [dkyq, 74]
#   # [lwnz, 85]
#   # [grn, 53]
#   # [pptcb, 11]
#   # [gvzn, 60]
#   # [omq, 77]
#   # [vpo, 31]
#   # [calh, 24]
#   # [hqwij, 92]
#   # [xwpr, 77]
#   # [wyw, 97]
#   # [nyej, 1]
#   # [kdhn, 37]
#   # [kta, 24]
#   # [dhagz, 81]
#   # [phvub, 37]
#   # [tged, 76]
#   # [gzv, 70]
#   # [lqce, 69]
#   # [ovytd, 51]
#   # [ubeak, 81]
#   # [glsqh, 8]
#   # [fjco, 90]
#   # [osq, 92]
#   # [fiq, 41]
#   # [jigib, 31]
#   # [jmfip, 53]
#   # [ptwuv, 69]
#   # [suqup, 13]
#   # [gors, 93]
#   # [uhe, 84]
#   # [qzm, 24]
#   # [ojqk, 89]
#   # [rsz, 42]
#   # [gytbh, 45]
#   # [iyto, 70]
#   # [tzaup, 49]
#   # [isx, 91]
#   # [vuhzw, 29]
#   # [ghr, 80]
#   # [bip, 55]
#   # [inlt, 38]
#   # [xgrju, 66]
#   # [nqyqt, 5]
#   # [pwtu, 27]
#   # [mjl, 27]
#   # [bexl, 41]
#   # [fkuw, 25]
#   # [fal, 9]
#   # [doc, 88]
#   # [xgx, 25]
#   # [ygwkt, 48]
#   # [lwij, 18]
#   # [dal, 50]
#   # [ycqm, 17]
#   # [uvjl, 87]
#   # [lhhq, 34]
#   # [eiplc, 76]
#   # [uqs, 69]
#   # [pyi, 74]
#   # [ncpb, 71]
#   # [iyh, 51]
#   # [womz, 85]
#   # [iyjib, 68]
#   # [xhi, 36]
#   # [jpv, 64]
#   # [waigf, 16]
#   # [tcc, 9]
#   # [cff, 54]
#   # [qzdy, 47]
#   # [lpto, 90]
#   # [utri, 70]
#   # [vjybg, 46]
#   # [zdqpb, 19]
#   # [ftt, 37]
#   # [jarx, 24]
#   # [hcr, 53]
#   # [wgvlc, 31]
#   # [upeq, 63]
#   # [kynb, 20]
#   # [dgvd, 26]
#   # [mdnm, 15]
#   # [che, 10]
#   # [ttan, 41]
#   # [come, 71]
#   # [pfw, 84]
#   # [lhti, 75]
#   # [aelc, 45]
#   # [rnbv, 36]
#   # [rfgsu, 51]
#   # [bsiga, 27]
#   # [aibm, 70]
#   # [xtqsj, 45]
#   # [ubo, 53]
#   # [aouo, 68]
#   # [abp, 50]
#   # [wph, 83]
#   # [frfdd, 40]
#   # [yejev, 28]
#   # [upexg, 59]
#   # [jzh, 15]
#   # [tfaw, 36]
#   # [ctp, 0]
#   # [gvv, 0]
#   # [bwrrn, 30]
#   # [znc, 46]
#   # [uasc, 46]
#   # [kjta, 53]
#   # [yzvv, 19]
#   # [sgu, 80]
#   # [acv, 99]
#   # [ssol, 23]
#   # [plx, 71]
#   # [wth, 47]
#   # [rky, 50]
#   # [qanl, 57]
#   # [mesxq, 96]
#   # [fine, 75]
#   # [eahuj, 38]
#   # [iscly, 3]
#   # [bnyav, 25]
#   # [hjau, 70]
#   # [qkdz, 75]
#   # [syp, 13]
#   # [lwy, 71]
#   # [evu, 33]
#   # [qfjvf, 33]
#   # [dnyii, 56]
#   # [fnsi, 39]
#   # [zngcu, 68]
#   # [azk, 99]
#   # [ulzai, 69]
#   # [jdnf, 16]
#   # [lpyei, 74]
#   # [nwzep, 73]
#   # [yts, 45]
#   # [atrz, 45]
#   # [hwflk, 2]
#   # [umzb, 50]
#   # [kyyru, 34]
#   # [knbz, 33]
#   # [bijyz, 35]
#   # [pld, 50]
#   # [flb, 84]
#   # [ruv, 69]
#   # [fmd, 4]
#   # [xwycn, 60]
#   # [alflu, 31]
#   # [ldln, 17]
#   # [wcdc, 96]
#   # [unfg, 0]
#   # [qpt, 83]
#   # [ogml, 54]
#   # [fmr, 42]
#   # [xqs, 6]
#   # [mcn, 48]
#   # [efkfm, 29]
#   # [pixb, 98]
#   # [ifa, 1]
#   # [vvd, 98]
#   # [zwyld, 58]
#   # [plthw, 70]
#   # [iedw, 32]
#   # [tiedr, 25]
#   # [mstr, 14]
#   # [xks, 69]
#   # [qzylh, 8]
#   # [xveg, 49]
#   # [wsipz, 29]
#   # [jrx, 91]
#   # [oive, 91]
#   # [axji, 78]
#   # [fvp, 15]
#   # [peua, 98]
#   # [qcr, 26]
#   # [sjwc, 69]
#   # [omsyl, 38]
#   # [jiu, 34]
#   # [aytv, 84]
#   # [oanz, 33]
#   # [dqnoy, 82]
#   # [msszf, 41]
#   # [cjif, 32]
#   # [rzb, 18]
#   # [znjtx, 36]
#   # [ygdam, 28]
#   # [dvckk, 78]
#   # [huw, 34]
#   # [oqzwm, 19]
#   # [qsoip, 56]
#   # [kkla, 94]
#   # [uvnpd, 86]
#   # [jrir, 10]
#   # [yyg, 17]
#   # [eduno, 91]
#   # [vnlp, 0]
#   # [nkcof, 55]
#   # [ulsy, 33]
#   # [wufl, 53]
#   # [kfplc, 96]
#   # [ucj, 68]
#   # [iyudz, 17]
#   # [kiq, 42]
#   # [gncd, 22]
#   # [jtlol, 98]
#   # [xtzic, 22]
#   # [vcn, 13]
#   # [kwi, 25]
#   # [vlws, 52]
#   # [djvx, 93]
#   # [rgxq, 58]
#   # [pdac, 10]
#   # [realn, 64]
#   # [abxxd, 4]
#   # [mqrox, 58]
#   # [rhi, 13]
#   # [oocs, 42]
#   # [dge, 26]
#   # [qoob, 9]
#   # [lgfeb, 2]
#   # [qika, 10]
#   # [yabj, 91]
#   # [iur, 50]
#   # [med, 97]
#   # [jqto, 50]
#   # [punjn, 1]
#   # [ifzp, 96]
#   # [zpfrz, 51]
#   # [afni, 85]
#   # [yapa, 74]
#   # [zcmy, 44]
#   # [phrla, 34]
#   # [ysz, 48]
#   # [ucbtm, 60]
#   # [jtgt, 92]
#   # [wrt, 24]
#   # [pwhs, 56]
#   # [dneln, 20]
#   # [muuy, 73]
#   # [ozb, 12]
#   # [aux, 38]
#   # [rvehn, 42]
#   # [pfaz, 38]
#   # [tvw, 6]
#   # [lanz, 37]
#   # [voy, 68]
#   # [ftwe, 94]
#   # [gaust, 35]
#   # [zubc, 16]
#   # [sfyct, 66]
#   # [ufbpi, 21]
#   # [ncg, 18]
#   # [bdeg, 29]
#   # [dywl, 55]
#   # [hll, 71]
#   # [lluf, 24]
#   # [dsrw, 22]
#   # [kks, 46]
#   # [ghr, 67]
#   # [grt, 85]
#   # [ebtsp, 34]
#   # [mtu, 93]
#   # [hmtb, 89]
#   # [usfom, 75]
#   # [ebyf, 28]
#   # [uyv, 36]
#   # [fyumr, 4]
#   # [laon, 85]
#   # [ohakl, 75]
#   # [vid, 43]
#   # [fcy, 16]
#   # [lqxct, 50]
#   # [kohh, 64]
#   # [srf, 88]
#   # [mmy, 76]
#   # [xkhtj, 22]
#   # [csa, 23]
#   # [tlm, 9]
#   # [zsex, 44]
#   # [nox, 12]
#   # [dvu, 2]
#   # [makqt, 11]
#   # [cnq, 60]
#   # [yxa, 57]
#   # [hnsuy, 31]
#   # [ciza, 84]
#   # [clzh, 19]
#   # [ouvbe, 18]
#   # [veei, 46]
#   # [iufm, 0]
#   # [xitba, 52]
#   # [rgh, 81]
#   # [zbek, 52]
#   # [eiyhm, 84]
#   # [pcx, 80]
#   # [iffja, 92]
#   # [xaix, 72]
#   # [bvgrb, 2]
#   # [dgiym, 82]
#   # [dtl, 34]
#   # [bff, 14]
#   # [thmfe, 59]
#   # [bnj, 33]
#   # [uizx, 27]
#   # [giqkg, 98]
#   # [txex, 2]
#   # [omi, 76]
#   # [eby, 60]
#   # [ruq, 17]
#   # [zxj, 19]
#   # [gkw, 17]
#   # [qcy, 92]
#   # [fdyfd, 80]
#   # [lwfh, 77]
#   # [fmvg, 17]
#   # [zvijt, 84]
#   # [gtm, 78]
#   # [zmp, 58]
#   # [zxvf, 89]
#   # [efvc, 54]
#   # [kgwgo, 46]
#   # [xfkky, 67]
#   # [mis, 48]
#   # [adak, 97]
#   # [xuhw, 22]
#   # [gnp, 25]
#   # [uapqb, 6]
#   # [flgo, 87]
#   # [bej, 84]
#   # [vism, 77]
#   # [ayptr, 14]
#   # [xojhr, 14]
#   # [bsgol, 93]
#   # [wwj, 20]
#   # [muoe, 88]
#   # [wnh, 63]
#   # [ndi, 88]
#   # [vqijy, 54]
#   # [pms, 47]
#   # [gndz, 61]
#   # [fxv, 75]
#   # [dvicr, 22]
#   # [ujf, 39]
#   # [jenm, 67]
#   # [enyb, 62]
#   # [vatj, 12]
#   # [oxav, 20]
#   # [aqs, 9]
#   # [zey, 25]
#   # [axdbo, 90]
#   # [sfnk, 21]
#   # [euf, 10]
#   # [ggohu, 26]
#   # [klgn, 87]
#   # [baoj, 2]
#   # [wbxa, 56]
#   # [chmrk, 68]
#   # [vkbk, 91]
#   # [owz, 38]
#   # [euw, 26]
#   # [dmre, 29]
#   # [syhrm, 32]
#   # [kvga, 52]
#   # [icqoj, 93]
#   # [twwj, 40]
#   # [ugygf, 54]
#   # [snj, 41]
#   # [bfvpe, 3]
#   # [uxv, 39]
#   # [npwi, 43]
#   # [nzu, 84]
#   # [yrzaq, 22]
#   # [cman, 17]
#   # [zyzxd, 79]
#   # [sjxln, 60]
#   # [skpvs, 5]
#   # [ecil, 60]
#   # [atwtg, 93]
#   # [lgchj, 77]
#   # [fnyz, 1]
#   # [cpov, 68]
#   # [fwyc, 11]
#   # [yovei, 67]
#   # [ift, 53]
#   # [gpn, 54]
#   # [wfzid, 81]
#   # [rzei, 41]
#   # [dcmd, 67]
#   # [gatnk, 42]
#   # [abi, 22]
#   # [oozh, 15]
#   # [hksdy, 20]
#   # [hwvy, 85]
#   # [ymeg, 97]
#   # [jgnn, 84]
#   # [pgfay, 83]
#   # [emxn, 39]
#   # [wyb, 17]
#   # [fef, 0]
#   # [owfz, 49]
#   # [zzpb, 61]
#   # [evl, 97]
#   # [hmu, 90]
#   # [ebd, 62]
#   # [ysjo, 71]
#   # [kqpaj, 28]
#   # [sky, 31]
#   # [ynb, 7]
#   # [yypt, 11]
#   # [ziyl, 18]
#   # [wcxyk, 53]
#   # [lph, 9]
#   # [zqk, 68]
#   # [uond, 84]
#   # [zec, 60]
#   # [cnwz, 95]
#   # [ajuuf, 23]
#   # [rtt, 8]
#   # [rjr, 31]
#   # [qs...]
# ]

highestScore(A)
