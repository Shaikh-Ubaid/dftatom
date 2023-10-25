#!/usr/bin/env bash

git clean -dfx

echo "RUN lfortran"
time make -f Makefile.manual F90=lfortran F90FLAGS="-I../../src"
cd tests/lda
time ./conv_lda
cd ../rlda
time ./conv_rlda
cd ../..

echo "RUN lfortran --fast"
git clean -dfx
time make -f Makefile.manual F90="lfortran --skip-pass=inline_function_calls,fma --fast" F90FLAGS="-I../../src"
cd tests/lda
time ./conv_lda
cd ../rlda
time ./conv_rlda
cd ../..


echo "RUN gfortran"
git clean -dfx
time make -f Makefile.manual
cd tests/lda
time ./conv_lda
cd ../rlda
time ./conv_rlda
cd ../..

echo "RUN gfortran -fast"
git clean -dfx
time make -f MakefileRelease.manual
cd tests/lda
time ./conv_lda
cd ../rlda
time ./conv_rlda
cd ../..
