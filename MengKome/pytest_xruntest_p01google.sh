#!/bin/bash

torun="$1"

onbrowser="$2"
if [ x"$onbrowser" == x ]; then
# onbrowser='firefox'
onbrowser='chrome'
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

#if [ x"$torun" == xtestsuite -o x"$torun" == xtest_suite -o x"$torun" == xsuite ]; then
#
#file1=console_${masani}_test_suite.txt
#echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > "$file1"
#echo "$ py.test.exe -v tests/test_suite_PixitMedia.py > consoleoutput1.txt 2>&1" >> "$file1"
#echo >> "$file1"
#echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> "$file1"
#echo "$ cat consoleoutput1.txt" >> "$file1"
#echo >> "$file1"
#
#py.test.exe -v tests/test_suite_PixitMedia.py --browser "$onbrowser" | tee -a "$file1"
#
#elif [ x"$torun" == xp01 ]||[ x"$torun" == xgoogle ]; then

if [ x"$torun" == xp01 ]||[ x"$torun" == xgoogle ]; then

file1=console_${masani}_p01maingithubcromox1.txt
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > "$file1"
echo "$ py.test.exe -v -s tests/p01google/p01searchgithubcromox1_test1.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

# py.test.exe -v -s tests/p01google/p01searchgithubcromox1_test1.py --browser "$onbrowser" | tee -a "$file1"
py.test.exe -v -s tests/p01google/p01searchgithubcromox1_test1.py | tee -a "$file1"

#elif [ x"$torun" == xp02 ]||[ x"$torun" == xproducts ]; then
#
#file1=console_${masani}_pixitmedia.txt
#echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > "$file1"
#echo "$ py.test.exe -v -s tests/p01google/p02_test1.py > consoleoutput1.txt 2>&1" >> "$file1"
#echo >> "$file1"
#echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> "$file1"
#echo "$ cat consoleoutput1.txt" >> "$file1"
#echo >> "$file1"
#
#py.test.exe -v -s tests/p01google/p01searchgithubcromox1_test1.py --browser "$onbrowser" | tee -a "$file1"

elif [ x"$torun" == xp01test1 ]||[ x"$torun" == xtest1 ]; then

# tests/p01google/p01searchgithubcromox1_test1.py::P01SearchGitHubCromox1Tests::test1_google_github_cromox1_page

file1=console_${masani}_p01test1githubcromox1.txt
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > "$file1"
echo "$ py.test.exe -v -s tests/p01google/p01searchgithubcromox1_test1.py::P01SearchGitHubCromox1Tests::test1_google_github_cromox1_page > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

# py.test.exe -v -s tests/p01google/p01searchgithubcromox1_test1.py::P01SearchGitHubCromox1Tests::test1_google_github_cromox1_page --browser "$onbrowser" | tee -a "$file1"
py.test.exe -v -s tests/p01google/p01searchgithubcromox1_test1.py::P01SearchGitHubCromox1Tests::test1_google_github_cromox1_page | tee -a "$file1"

else

echo
# echo "./pytest_xruntest_p01google.sh test_suite  [ testsuite / test_suite / suite ] [ ie / chrome / firefox / opera ] "
echo "./pytest_xruntest_p01google.sh p01         [ p01 / google ]                   [ ie / chrome / firefox / opera ] "
echo "./pytest_xruntest_p01google.sh p01test1    [ p01test1 / test1 ]               [ ie / chrome / firefox / opera ] "
echo

fi
