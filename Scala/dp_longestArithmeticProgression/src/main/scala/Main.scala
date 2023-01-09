//Problem Description
//Find the longest Arithmetic Progression in an integer array A of size N, and return its length.
//More formally, find longest sequence of indices, 0 < i1 < i2 < … < ik < ArraySize(0-indexed) such that sequence A[i1], A[i2], …, A[ik] is an Arithmetic Progression.
//Arithmetic Progression is a sequence in which all the differences between consecutive pairs are the same, i.e sequence B[0], B[1], B[2], …, B[m - 1] of length m is an Arithmetic Progression if and only if B[1] - B[0] == B[2] - B[1] == B[3] - B[2] == … == B[m - 1] - B[m - 2]
//Note: The common difference can be positive, negative, or 0.
//Problem Constraints
//1 <= N <= 1000
//1 <= A[i] <= 1e9
//Input Format
//The first and only argument of input contains an integer array, A.
//
//
//Output Format
//Return an integer, representing the length of the longest possible arithmetic progression.
//
//
//Example Input
//Input 1:

//
//
//Example Output
//Output 1:
//4
//Output 2:
//3
//
//
//Example Explanation
//Explanation 1:
//[3, 6, 9, 12] form an arithmetic progression.
//Explanation 1:
//[4, 7, 10] form an arithmetic progression.
object Main {
  import scala.math
  import scala.util.Sorting
  def main(args: Array[String]): Unit = {
    def solve(A: Array[Int]): Int = {
      val n_A = A.length
      if (n_A <= 2){
        return n_A
      }
      val each = 2
      var result = each
//      var longLap = Array.fill(n_A)(each)
      var longLap = Array.ofDim[Int](n_A,n_A)
      scala.util.Sorting.quickSort(A)
//      A.sorted
      for (i<-0 to n_A - 1){
        for (j<-0 to n_A - 2){
          longLap(i)(j) = 0
        }
        longLap(i)(n_A - 1) = 2
      }

      var left: Int = -99
      var right: Int = -99
      var i: Int = 0

      for (i <- n_A - 2  to 1 by -1){
//        println(i)
        left = i - 1
        right = i + 1
        while(left >= 0 && right <= n_A - 1){
//          println(left, right, result, longLap(i), longLap(right))
          var curr_left = BigInt(A(left))
          var curr_right = BigInt(A(right))
          var curr_twice = BigInt(2 * A(i))
          if (curr_left + curr_right == curr_twice) {
            //            println("here")
            longLap(left)(i) = longLap(i)(right) + 1
//              longLap(i).max(longLap(right) + 1)
            result = result.max(longLap(left)(i))
            left -= 1
            right += 1
            while(left >= 0){
              longLap(left)(i) = 2
              left -= 1
            }
          } else if (A(left) + A(right) < 2 * A(i)) {
            //            println("there")
            right += 1
          } else {
            //            println("!")
            longLap(left)(i) = 2
            left -= 1
          }
        }

      }
      result
//      var longLap: Array[Int] = Array()
//      longLap.fill(n_A)(each)

    }

    var A = Array(3, 6, 9, 12)
    var A2 = Array(9, 4, 7, 2, 10)
    var A3 = Array(100, 10, 8, 300, 6, 1, 4, 2 )
    var A4 = Array(364702938, 643942025, 489766715, 204360054, 853076025, 958774974, 487442754, 873986593, 304523071, 665723496, 424996402, 383918492, 403477633, 568954025, 739359908, 7841987, 803773042, 267635441, 244349842, 799061430, 536467496, 199104939, 577187747, 610830330, 179781827, 83666657, 657448834, 939189223, 948465511, 88731696, 959963654, 64492867, 526115758, 163619780, 104832477, 982841996, 181205645, 391455666, 379217474, 850363046, 548034934, 265765352, 3008858, 104010702, 56171453, 254539311, 254775153, 997346177, 213581777, 150010079, 73587772, 912836752, 424116696, 631085279, 228551620, 492574681, 153195979, 352870327, 415486295, 535081845, 532788699, 646597927, 30355042, 149824732, 179686213, 624174209, 38315068, 789995600, 638393219, 646531321, 922600653, 243493404, 363551670, 621933572, 788319202, 380459444, 249316366, 519559662, 570722129, 391104374, 917512175, 620789538, 60466217, 495935685, 807015385, 852840, 375029771, 260857252, 139969014, 964616430, 954279404, 92317005, 14968078, 312891844, 659504025, 47304185, 472479502, 642196928, 150959074, 990969611, 416827769, 532648666, 440538539, 681351941, 25516356, 430407716, 63809489, 851741770, 97937488, 102688129, 376265335, 625886754, 903763069, 394057049, 77246792, 132960129, 204153400, 601059314, 240814910, 443259599, 243300547, 343421138, 516756650, 705148082, 535308205, 42253925, 418372142, 719121913, 244018072, 591703754, 841966045, 79818005, 397672484, 712320721, 826759242, 49642381, 42092204, 921552765, 885259191, 784516721, 896679091, 518981211, 512380987, 177815636, 323891048, 839540415, 114443888, 386819728, 846160624, 784888731, 706591816, 104083602, 207668333, 620737953, 267210542, 619265114, 209267409, 652871101, 236891757, 5078361, 526409271, 801725477, 213948838, 950486785, 774278882, 628010778, 95012438, 219945518, 804964539, 965772697, 744471141, 12989138, 338852196, 651816584, 767235538, 362120351, 188083659, 26128429, 554728873, 27906657, 875749153, 936839757, 115687692, 890330506, 118753643, 880161435, 650786955, 642130111, 101699175, 934793037, 76203004, 843626213, 64974170, 25440691, 232439481, 337594871, 305193120, 116068577, 849422163, 840750109, 44676300, 329031070, 254802465, 382637137, 342580618, 348780716, 400870922, 781385415, 882168500, 378880612, 557432529, 371104866, 866963571, 380184499, 997016465, 40821311, 842405023, 958020556, 692841310, 927554733, 828595555, 847775510, 8998725, 917715785, 821645741, 6376954, 877016948, 769833852, 8568986, 137534950, 857492075, 106541105, 708723557, 498774414, 199151630, 288181561, 891863339, 111274110, 799443653, 518038516, 774625071, 3949956, 888659259, 592783236, 731200616, 313574751, 325970319, 352367936, 561743750, 889085635, 671043216, 712950688, 677204780, 117399957, 677339126, 227877935, 981110944, 78452319, 966782539, 852851368, 493331671, 696455124, 461642691, 584195365, 276265471, 334126283, 486013363, 472540577, 594942630, 516913575, 121352683, 538820355, 15158683, 295164608, 144342086, 374660116, 490508205, 855414022, 614192913, 860131082, 436925394, 84757638, 739963905, 495551558, 793452240, 752091634, 315337993, 969740975, 109427919, 909024398, 774384025, 247657128, 550042410, 719426359, 921233046, 880451076, 505156275, 84915511, 172101542, 923885709, 366593126, 200085439, 950323895, 184070299, 219321790, 177019445, 900952617, 403430519, 850850851, 156638981, 890135865, 68656230, 706530768, 151783286, 884856990, 467167052, 476421129, 317128860, 645885401, 939832442, 313254675, 315153701, 19837382, 546905586, 612166339, 85498393, 304922905, 943274190, 885020773, 806178951, 975300534, 133397387, 36955841, 494045704, 180626003, 313088983, 751602131, 678204063, 806230389, 766068773, 79662223, 99254055, 641850490, 770818146, 445470891, 901271595, 395793051, 263203171, 913124001, 956934942, 700529408, 218657175, 626620208, 346030968, 356763100, 343079276, 139799537, 263708541, 816943003, 424345923, 188736174, 255529799, 795779617, 139861000, 222966955, 46648670, 192665535, 798048893, 698618909, 321163591, 96318799, 701126779, 594995161, 326060268, 790398956, 975146570, 766949910, 930279673, 455763724, 366902932, 38285764, 297474868, 318176260, 354120790, 970900255, 266094056, 108095911, 86458880, 341708965, 731294274, 813942934, 468051945, 316432251, 33582358, 704233569, 197465339, 937717958, 916976597, 209264680, 607004798, 308566509, 978051082, 190950809, 969678245, 128866632, 124226025, 512688888, 574088074, 54225344, 832281877, 526763601, 314507250, 966087080, 975432013, 195681293, 992598809, 955212967, 750333221, 826461760, 418563121, 707680495, 147900556, 52314886, 935477379, 840529166, 626262996, 784819825, 622238901, 797590041, 502886110, 584949598, 67757620, 635986430, 997817891, 625494614, 755525433, 45147720, 736002649, 490715023, 36445258, 502603408, 128544378, 76812164, 344368501, 332967642, 918516836, 326257789, 888908932, 922429769, 592671487, 922843327, 27148028, 119332972, 953267526, 265561039, 813355604, 260473046, 125069713, 733909398, 742925642, 881333033, 295822045, 456467510, 267616445, 998825894, 387123456, 582208002, 160652059, 692202931, 935737115, 910936421, 697499881, 841004414, 23821544, 936731666, 446494305, 921921517, 640423114, 403238234, 840350730, 848506211, 478730374, 473903929, 960229804, 242700220, 991143484, 117877406, 111889881, 411297019, 992872060, 179033407, 389873599, 632962993, 648769533, 21323489, 827843994, 27458245, 855481434, 673436170, 129139273, 411536018, 714760959, 210342443, 467348136, 298674446, 78389060, 3705582, 2690911, 128984590, 371843578, 397594273, 471570267, 393078216, 805869737, 73299727, 366631731, 848919674, 985352074, 492155474, 623785098, 3906914, 165243961, 558896956, 287667514, 842218401, 26206407, 216926411, 528690491, 487492775, 640947717, 630297864, 953103017, 721883746, 491255296, 526870577, 722185343, 191486957, 317041270, 605688280, 730426777, 192564560, 174703891, 638150588, 863599398, 746853937, 332194041, 801498307, 690869942, 7027462, 519629318, 667697101, 309370705, 535529548, 541148659, 492266768, 346819709, 728222802, 731320558, 181956298, 122787158, 377324645, 176098924, 462150102, 982154939, 444998704, 481417451, 538450481, 241145709, 634289274, 391004410, 311159050, 527472905, 424619519, 492096852, 712266967, 997065991, 873213196, 190941574, 814465600, 662573222, 91690636, 224994126, 831315139, 384925388, 146501125, 154406590, 951304151, 553105539, 661819530, 309291074, 270904751, 430818417, 524018659, 351157063, 611687482, 627283382, 754569748, 89068874, 184463359, 383030269, 507490797, 666521119, 945735878, 382679872, 922966944, 595387022, 469617154, 853104553, 453653076, 980293079, 291230566, 596882846, 913869182, 596290127, 615717360, 711716451, 334469764, 394869122, 840864224, 888873685, 330025036, 854261675, 574041303, 341895374, 643044866, 443609335, 752604381, 343150637, 265422041, 624699865, 283072469, 922699975, 839056435, 570126616, 46002198, 64828866, 804541833, 303803896, 389700926, 952081756, 737410892, 536726604, 258965801, 562606762, 361342790, 4509411, 627734629, 822485312, 158403045, 473996859, 374612263, 759993061, 391541083, 741079170, 986191010, 633517524, 305104042, 766426682, 726321265, 984442904, 244120813, 170996498, 605013797, 131809231, 188355133, 293824653, 172296695, 982588306, 212405109, 774837246, 348749711, 953511711, 74602636, 789795228, 491966486, 668680849, 737095989, 612861000, 814345140, 785485649, 1582811, 832492310, 842285562, 81231107, 525349277, 166283899, 857257343, 456367675, 433660061, 493857994, 247009503, 402827270, 375729723, 213782054, 294840147, 59835177, 627464640, 579747483, 682640342, 204843897, 395082335, 129359418, 890279159, 329506437, 728102870, 863107081, 643548733, 322159012, 720240597, 792137464, 129479468, 760484265, 710116735, 291588539, 170892519, 986712927, 815433552, 824806730, 519769725, 880033903, 55509912, 947179783, 137385868, 499362951, 427024981, 118507393, 759850457, 795123914, 930620737, 819325658, 741189442, 692057271, 635113142, 279101777, 759280991, 887785263, 290535885, 732547741, 406126333, 688375227, 443157037, 667033063, 960052501, 484002573, 734981560, 509141376, 490514961, 968962114, 977754797, 580006335, 738198612, 891043165, 285261801, 137839076, 600237043, 379541515, 927811015, 840968238, 489553336, 913058092, 922944202, 648820733, 881841889, 258230249, 11344356, 612288533, 580840980, 807425018, 443112133, 986073359, 803632411, 51525467, 552614128, 992617845, 201400792, 508883472, 450889727, 707584846, 687811460, 142728016, 90522810, 998437191, 296643076, 296883418, 41352522, 300869046, 455809261, 712072375, 947775314, 299750776, 988389790, 7449162, 644005805, 487975352, 161684768, 869073918, 415306352, 732005314, 953240559, 886060090, 286574105, 718904338, 882202341, 947637896, 137641693, 504046432, 759137033, 615758401, 327742311, 69458019, 223554785, 262631069, 961473695, 747681610, 284258850, 461110795, 694391366, 135800337, 694889022, 983711965, 844130922, 822768820, 628354707, 506726427, 704648007, 720482268, 558926263, 780230263, 794881659, 80274826, 559270266, 119437743, 566678480, 75230512, 605080521, 179506079, 817879138, 51847919, 603355775, 182720888, 88341003, 836028941, 152900663, 337251002, 968246181, 756228925, 57569302, 125875741, 322178289, 981487844, 50242752, 468851190, 864441084, 934418430, 222634096, 894729995, 991873943, 583541760, 28544471, 858070816, 169773084, 444189345, 837164443, 983680181, 309937234, 393506040, 480114940, 121992978, 562831781, 922020056, 149076037, 481271230, 228406185, 195723879, 660028973, 280162229, 328686756, 910359605, 666629780, 624526061, 583182515, 433156294, 88261525, 573984018, 452848202, 337686046, 763837925, 166755306, 190260204, 100089842, 730270490, 787074422, 934278454, 17549514, 749422159, 546636658, 387269140, 883243747, 196937538, 656901139, 324013946, 757603454, 610699912, 135321744, 167369235, 844896899, 510480984, 456719920, 985132659, 25673040, 916303653, 710263334, 608002689, 973993194, 709503897, 729046912, 623493622, 410849418, 986234818, 296048353, 79558459, 330441752, 341814722, 361276929, 317431825, 727303627, 315140265, 867760353, 886806094, 250484142, 819026474, 7771248, 688604493, 586331765, 749251692, 902823260, 704814538, 298143314, 815329947, 157267722, 719976021, 640367522, 542645314, 950477009, 609982054, 955184220, 267182392, 146148064, 662952900, 30487841, 234285474, 224694744, 94560755, 144710505, 124227308, 534252269, 548748573, 448735966, 918966342, 364920770, 10085558, 930507017, 648769187, 15508267, 801913779, 157506678, 441133815, 644796333, 889485969, 957014216, 959154106, 417054933, 55635123, 904125816, 48303340, 85416814, 7574879, 609447777, 565525269, 20574461, 50098860, 197950396, 500136369, 540959425, 533036401, 514749743, 261058662, 303833010, 879019924, 74113132, 78885861, 837247225, 227505204, 85330145, 698404239, 704098132, 68659327, 758590450, 19280911, 857982304)
    var A5 = Array(95142543, 259145010, 353338551, 768734299, 855734538, 632387804, 645244422, 904316624, 33987926, 4413777, 94155814, 855059883, 30879454, 373674224, 26757117, 882774793, 905162248, 287746788, 27092872, 83366540, 982099936, 594313510, 680720373, 148179619, 447559433, 569916814, 814818875, 157606803, 423412573, 608041673, 555463862, 569706722, 505028101, 78178740, 763824636, 319328823, 397894308, 145557798, 406037053, 635461429, 764052269, 548009443, 911088342, 29610657, 523847919, 702755353, 49159371, 514086126, 918799398, 780310029, 602562236, 804363024, 519778100, 71916185, 735769858, 873155577, 296272461, 510416458, 445973261, 754669597, 693497597, 146618687, 478172256, 757299518, 871165081, 128002718, 636800552, 722122640, 211371056, 575386054, 394547137, 797971447, 470725811, 158941526, 934304034, 447472574, 183819424, 297832959, 967894176, 208790007, 145368451, 444907495, 22201208, 547281698, 491038185, 99119874, 534154070, 708027714, 614901171, 952671633, 987805623, 926764224, 427421077, 333241924, 159665292, 213745718, 757874415, 869782548, 514099107, 63237645, 904427670, 826596224, 531024325, 345138970, 397338243, 463449755, 276836213, 262902262, 150713732, 88723684, 825305970, 320561817, 719729820, 797434609, 38032536, 336447570, 349858036, 253777163, 330247196, 293129097, 293247061, 128384362, 608648723, 20726573, 459161597, 146475285, 793847130, 946548519, 82101857, 127667402, 369853658, 239005361, 94940614, 86541374, 654435396, 758194058, 873313332, 800177099, 483775153, 435900526, 39670338, 33096583, 55997505, 552220746, 823489108, 923075065, 700743124, 589356517, 46651028, 232296441, 81013641, 91632089, 314744924, 665715107, 284002479, 447259096, 890853569, 319938896, 987706404, 332940718, 466005168, 275989564, 501196756, 109272735, 448330557, 645287596, 556208622, 201994563, 824716258, 72940241, 767209874, 648085595, 337537581, 416070317, 687054784, 310176366, 117621866, 112004799, 195231794, 979490966, 768761080, 232109385, 158380516, 95351956, 557515427, 690621325, 123488837, 888162933, 195576231, 325984280, 587010463, 344977323, 901762585, 57918989, 634356032, 439264293, 739927485, 957182442, 565294614, 438914767, 234153121, 147713116, 123244680, 125359229, 231095693, 301128248, 517249981, 406619208, 756055699, 367385391, 630773009, 348930444, 769874175, 686277647, 133736689, 370887034, 427095021, 221919446, 694775907, 156329983, 395735667, 372500510, 701240565, 359921219, 808235958, 113928604, 316376128, 164064921, 70116096, 546436689, 247615628, 926285330, 968584207, 470691215, 651236781, 686162928, 353146506, 762267858, 622184824, 962459725, 140027048, 866252044, 232718672, 734990714, 662984251, 557395694, 825760844, 449436371, 977092495, 186106453, 81215312, 259891116, 8240211, 135300262, 880054681, 285404855, 394664007, 614721890, 86971110, 360815583, 807426177, 462583043, 742393158, 521809033, 794936703, 271530119, 203951755, 433237270, 375483333, 367681022, 230734108, 666428498, 462796554, 35913644, 157709901, 635485709, 98392809, 125524270, 857456133, 576205734, 212265192, 570735874, 622116589, 889375904, 180885181, 374134739, 250431554, 276267334, 365437724, 108596848, 899866210, 397799069, 692359572, 347185335, 430848043, 77873953, 67828025, 745533038, 680431245, 657506037, 826849817, 498194582, 117600021, 818597707, 317677044, 553723663, 313211363, 660959144, 881169101, 761842392, 987570527, 196731223, 410582001, 786732996, 564649193, 328750658, 910627099, 867434144, 772920549, 347077937, 773293504, 172881681, 77029773, 780489090, 850019754, 147043811, 685387200, 200387892, 664942348, 181143848, 426583714, 218317285, 282798096, 606280258, 142634310, 663089715, 182445495, 828528373, 792389460, 69808946, 752884160, 750428996, 288676941, 627788814, 659439187, 31313742, 156568279, 775597578, 242756156, 857526416, 683710292, 208128935, 845883002, 413871474, 238330885, 570182540, 985916866, 320946610, 744494830, 411130161, 335981705, 36257745, 572306291, 172569521, 199265770, 59048894, 297308141, 737212638, 425905500, 630734646, 777905327, 374379550, 70002737, 788695623, 264524654, 574702085, 710231809, 78162014, 482710754, 800165936, 846280435, 651068561, 6373035, 811158719, 918390674, 353336702, 737666559, 538762982, 124640899, 216609991, 579328669, 86075982, 348784816, 469788026, 503716383, 580712607, 797352058, 798073123, 32110696, 666063872, 776978313, 900191008, 487969938, 70691670, 556432496, 743411007, 448936403, 90331487, 931780874, 990395394, 429639061, 29935190, 609556529, 245836486, 15283374, 243371002, 453816499, 505726373, 2867782, 954163437, 290743283, 997060456, 780186451, 58533375, 222923299, 386664102, 378038089, 355783770, 350119260, 349210040, 100335029, 556169508, 618347389, 891190687, 617172004, 463856218, 665817316, 928087319, 116092045, 170107016, 687875352, 142819036, 546562530, 215133264, 456048324, 435036922, 557463439, 890609236, 508401459, 939623420, 729821726, 760890638, 23834981, 88825502, 389069046, 386639199, 98581296, 72208212, 275150126, 915867288, 892461140, 494847509, 771652352, 507335831, 209491204, 119217968, 94145525, 682132660, 262158707, 538686729, 990531971, 577605053, 108299508, 197431720, 372683425, 554267500, 863545234, 910261412, 90050256, 572423281, 426544421, 631661658, 252068658, 606441299, 501515228, 93114118, 527135983, 130680583, 546521020, 591224921, 310412578, 866419883, 906105098, 28090982, 752473958, 298606520, 10490198, 215090329, 808173199, 132879915, 90157901, 234120745, 677319911, 978673254, 984119202, 172370417, 74150313, 703786928, 206962817, 574290599, 236845952, 308967146, 195364376, 861162142, 586073234, 699096873, 838103371, 658107321, 195211770, 642947598, 956301302, 788368566, 136386772, 887425655, 689055170, 644675743, 511108396, 264215169, 741896807, 769580767, 49945088, 834729863, 867875010, 666362646, 429772217, 120404435, 707735168, 51718438, 574652255, 946480823, 18068605, 883850008, 722698157, 220417267, 143715394, 579265907, 104976871, 188454887, 896639904, 934115529, 500494510, 117775868, 552824362, 231053389, 663866744, 357070016, 132707371, 251008584, 954144482, 355447632, 782586894, 674323003, 1764379, 662880215, 956354693, 611960876, 927257449, 127119064, 817621707, 20163993, 667547545, 106731513, 687685343, 170563244, 839506583, 619579691, 127662334, 284684185, 93531779, 30580049, 710291910, 14537697, 595679545, 17342098, 484598514, 315493551, 362978811, 657568770, 807469928, 124172680, 689861296, 234591719, 3045341, 717180483, 900400590, 789197545, 110384716, 883792628, 832045917, 855959579, 119684597, 420577960, 211349620, 215102799, 726053865, 785218398, 878595968, 464869001, 507783618, 219246145, 861754183, 872838313, 332733934, 211811950, 469298748, 870355625, 482127835, 666714311, 971488351, 486547116, 853392660, 747848738, 945695499, 777771843, 278397609, 735481070, 314471358, 362858639, 785330017, 607092854, 714781878, 315493825, 367583929, 746375704, 884475001, 489537273, 643095654, 223461427, 841046810, 736362713, 99851327, 281258341, 497430140, 154525209, 797458440, 438560153, 716614967, 449829251, 64033890, 328282083, 551479838, 182216814, 206312276, 378074651, 970281304, 600802834, 225114441, 705957293, 177073776, 740360314, 715538277, 143389936, 477994015, 982820098, 886916186, 716335872, 663667219, 224878812, 998524097, 683530394, 131562332, 333690934, 189983598, 819881917, 426558044, 860623419, 121690361, 845465383, 911141706, 926499405, 271575438, 965636591, 920264558, 709200612, 756472252, 925940721, 545441458, 700637387, 959718405, 237551815, 361246529, 534134431, 715728954, 126872804, 973697181, 29380700, 953927914, 627275516, 622374289, 925572510, 799370122, 355944822, 548924636, 186601337, 882537936, 145532120, 220797725, 95613656, 660940033, 559962120, 448304891, 213919134, 451260060, 489329040, 364540690, 64531939, 109057038, 44344952, 128774352, 720751308, 785722653, 763675165, 652473456, 481825539, 954742960, 367109933, 296117697, 56773153, 703643203, 138712234, 243009616, 822461342, 829272675, 416979695, 938593704, 603254090, 621184740, 260166886, 348147710, 499365719, 473538354, 184711493, 258442709, 360934106, 651950187, 865225915, 166437745, 221721594, 590702813, 125278010, 726660066, 236228773, 673466332, 636072007, 288626883, 860205832, 619498417, 909165460, 997729412, 212161481, 975157147, 944717549, 447493545, 536279021, 252639488, 536704697, 964525079, 492693374, 585583, 178208666, 487103721, 544568080, 366794312, 360193071, 8535001, 640090878, 188056900, 650123336, 226112216, 295700946, 568631861, 693450274, 424994446, 351035597, 717692067, 908658290, 310422440, 175741129, 891132075, 705821944, 49738377, 581755153, 65803277, 1589931, 952158150, 947623026, 961471830, 716344959, 816392428, 834508310, 365459210, 469703647, 159300354, 522675289, 321724170, 928035464, 318315287, 543263932, 610179904, 807025690, 174057378, 509624832, 26025365, 395378987, 820230691, 919693544, 775844726, 101596895, 289506497, 611484397, 435267661, 140526518, 670918150, 758450073, 881190143, 41753462, 597025089, 83321812, 230356440, 761413363, 219331065, 141520976, 204904580, 341239692, 360424131, 670734950, 900641547, 543994550, 4766344, 651048669, 745798418, 845705611, 653678004, 913617000, 652834547, 696270503, 579943015, 747712792, 808334724, 700146943, 233018861, 411566523, 153716671, 93253753, 726497781, 729930249, 437353052, 829963107, 209901857, 578620402, 618090441, 867641348, 681772748, 655568664, 477684915, 82743692, 177570012, 490655774, 114389138, 540378301, 429761744, 503176133, 90665445, 174486569, 206836801, 603831738, 666038264, 346593061, 140175336, 137311393, 321403450, 906403542, 749071996, 30156235, 29692550, 826473343, 613238602, 927153458, 526817571, 147830813, 205422127, 449717533, 333881515, 171844591, 900269142, 727434656, 369852618, 221526081, 525941293, 452611996, 662730695, 590847296, 406120144, 958230042, 992447041, 551931838, 262788050, 378627891, 604917976, 668837734, 152645117, 337256674, 933040591, 687614140, 47596246, 12448015, 907865943, 631583663, 14948517, 636582067, 271270715, 139124424, 728244409, 20727583, 476136667, 904893547, 66656375, 380972715, 285919071, 447166135, 402199865, 568352123, 286861002, 172064696, 304606583, 995567857, 390128595, 623721874, 477752038, 137138130, 630589276, 482155384, 55988530, 401386324, 853812241, 536605233, 366575455, 976822362, 872443671, 142428378, 423216061, 526498363, 151619478, 279211177, 450483144, 316603710, 767810124, 355519245, 912444761, 278374900, 353819311, 258933031, 11832968, 234455829, 940359178, 210804550, 717787720, 368823018, 96908057, 941109573, 285142117, 273793735, 667590448, 664337381, 750881714, 381315603, 680128570, 939156429, 397296753, 839869148, 270758705, 123706942, 378403898, 61493096, 574821862, 575840201, 511203002, 780516387, 235058610, 333881210, 166726859, 785901702, 551726237, 28477513, 806449534, 154271494, 828237729, 202511449, 922084672, 161335325)


    println(solve(A))
    println(solve(A2))
    println(solve(A3))
    println(solve(A4)) // pass
    println(solve(A5)) // Expect 3 but indeed 2
//    println(A4.slice(655, 659))
//    var z: Int = 655
//    var zLeft: Int = 435
//    var zRight: Int = 868
//    while (z <= 659){
//      println(z, A4 (z))
//      z += 1
//    }
//    println(A4(657), A4(435), A4(868), A4(868) + A4(435))
//    (655, 633517524)
//    (656, 305104042)
//    (657, 766426682)
//    (658, 726321265)
//    (659, 984442904)
    //Input 2:
    // A = [9, 4, 7, 2, 10]
  }
}

