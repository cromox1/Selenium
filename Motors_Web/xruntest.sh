#!/bin/bash

torun="$1"
onbrowser="$2"

if [ x"$onbrowser" == x ]; then
onbrowser='firefox'
fi

date1=`date +%Y%m%d_%H`
minit=`date +%M`
minit2=$(((minit / 5 ) * 5))
if [ $minit2 -lt 10 ]; then
   minit1=0${minit2}
else
   minit1=${minit2}
fi
masani=${date1}${minit1}00

if [ x"$torun" == xtestsuite -o x"$torun" == xtest_suite -o x"$torun" == xsuite ]; then

file1=console_${masani}_test_suite.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/Motors_Web" > "$file1"
echo "$ py.test.exe -v tests/test_suite_Motors_Web.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/Motors_Web" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v tests/test_suite_Motors_Web.py --browser "$onbrowser" | tee -a "$file1"

elif [ x"$torun" == xlogin -o x"$torun" == xhome ]; then

file1=console_${masani}_login.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/Motors_Web" > "$file1"
echo "$ py.test.exe -v -s tests/home/login_tests.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/Motors_Web" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v -s tests/home/login_tests.py --browser "$onbrowser" | tee -a "$file1" 

else

echo
echo "./xruntest.sh test_suite  [ testsuite / test_suite / suite ] [ ie / chrome / firefox / opera / virtual ]"
echo "./xruntest.sh login       [ login / home ]                   [ ie / chrome / firefox / opera / virtual ]"
# echo "./xruntest.sh firewalloff [ firewalloff / fwoff /foff ]      [ ie / chrome / firefox / opera / virtual ]"
# echo "./xruntest.sh firewallon  [ firewallon / fwon /fon ]         [ ie / chrome / firefox / opera / virtual ]"
echo

fi
