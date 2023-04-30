if [[ $1 = 'ninewine' ]]; then
    wine64 ninewinecfg
else
    curDir=$(pwd)
    export WINEPREFIX="$curDir"
    winetricks galliumnine
fi
