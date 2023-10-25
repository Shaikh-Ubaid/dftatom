#!/usr/bin/env bash

git clean -dfx

echo "RUN lfortran"
time make -f Makefile.manual F90=lfortran F90FLAGS=""
cd tests/lda
time ./conv_lda
cd ../rlda
time ./conv_rlda
cd ../..

echo "RUN lfortran --fast"
git clean -dfx
time make -f Makefile.manual F90="lfortran --skip-pass=inline_function_calls,fma --fast" F90FLAGS=""
cd tests/lda
time ./conv_lda
cd ../rlda
time ./conv_rlda
cd ../..


echo "RUN gfortran"
git clean -dfx
time make -f Makefile.manual F90=gfortran F90FLAGS="-Wall -std=f95 -Wextra -Wimplicit-interface -fPIC"
cd tests/lda
time ./conv_lda
cd ../rlda
time ./conv_rlda
cd ../..

echo "RUN gfortran -fast"
git clean -dfx
time make -f Makefile.manual F90=gfortran F90FLAGS="-Wall -std=f95 -Wextra -Wimplicit-interface -fPIC -O3 -march=native -ffast-math -funroll-loops"
cd tests/lda
time ./conv_lda
cd ../rlda
time ./conv_rlda
cd ../..
