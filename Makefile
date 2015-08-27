
.PHONY: all clean pdf exec

all: uv.mk

bI$(EXE): bI.lpp bI.ypp bI.cpp bI.hpp
	flex bI.lpp
	bison -d bI.ypp
	$(CXX) $(CXXFLAGS) -o $@ lex.yy.c bI.cpp 

uv.html uv.mk : uv.bI bI$(EXE) 
	cat $< > uv.html
	cat $< > uv.mk
