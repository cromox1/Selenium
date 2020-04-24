#!/bin/bash

torun="$1"

onbrowser="$2"
if [ x"$onbrowser" == x ]; then
onbrowser='firefox'
fi

date1=`date +%Y%m%d_%H`
minit=`date +%M`
minit2=$(((10#$minit / 5 ) * 5))
if [ $minit2 -lt 10 ]; then
   minit1=0${minit2}
else
   minit1=${minit2}
fi
masani=${date1}${minit1}00

if [ x"$torun" == xtestsuite -o x"$torun" == xtest_suite -o x"$torun" == xsuite ]; then

file1=console_${masani}_test_suite.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/PixitMedia" > "$file1"
echo "$ py.test.exe -v tests/test_suite_PixitMedia.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/PixitMedia" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v tests/test_suite_PixitMedia.py --browser "$onbrowser" | tee -a "$file1"

elif [ x"$torun" == xp01 -o x"$torun" == xgoogle ]; then

file1=console_${masani}_p01mainpixitmedia.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/PixitMedia" > "$file1"
echo "$ py.test.exe -v -s tests/p01google/p01searchpixitmedia_tests.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/PixitMedia" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v -s tests/p01google/p01searchpixitmedia_tests.py --browser "$onbrowser" | tee -a "$file1"

elif [ x"$torun" == xp02 -o x"$torun" == xproducts ]; then

file1=console_${masani}_pixitmedia.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/PixitMedia" > "$file1"
echo "$ py.test.exe -v -s tests/p02pixitmediaproducts/p02pixitmediaproducts_tests.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/PixitMedia" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v -s tests/p02pixitmediaproducts/p02pixitmediaproducts_tests.py --browser "$onbrowser" | tee -a "$file1"

elif [ x"$torun" == xp01test1 -o x"$torun" == xtest1 ]; then

# tests/p01google/p01searchpixitmedia_tests.py::P01SearchPixitMediaTests::test1_google_pixitmedia_page

file1=console_${masani}_p01test1pixitmedia.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/PixitMedia" > "$file1"
echo "$ py.test.exe -v -s tests/p01google/p01searchpixitmedia_tests.py::P01SearchPixitMediaTests::test1_google_pixitmedia_page > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/PixitMedia" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v -s tests/p01google/p01searchpixitmedia_tests.py::P01SearchPixitMediaTests::test1_google_pixitmedia_page --browser "$onbrowser" | tee -a "$file1"

else

echo
echo "./xruntest.sh test_suite  [ testsuite / test_suite / suite ] [ ie / chrome / firefox / opera ] "
echo "./xruntest.sh p01         [ p01 / google ]                   [ ie / chrome / firefox / opera ] "
echo "./xruntest.sh p01test1    [ p01test1 / test1 ]               [ ie / chrome / firefox / opera ] "
echo

fi
