
.PHONY: all clean pdf exec

all: uv.mk

bI$(EXE): bI.lpp bI.ypp bI.cpp bI.hpp
	flex bI.lpp
	bison -d bI.ypp
	$(CXX) $(CXXFLAGS) -o $@ lex.yy.c bI.tab.cpp bI.cpp 

uv.html uv.mk : uv.bI bI$(EXE)
	./bI$(EXE) < $< > uv.html
