CXX := g++

CXXFLAGS := -std=c++0x -O3
CPPFLAGS := -Iinclude

SRC := src
OBJ := obj

SRCS := $(wildcard $(SRC)/*.cpp)
OBJS := $(SRCS:$(SRC)/%.cpp=$(OBJ)/%.o)

TARGET := program


.PHONY: all run clean

all: $(TARGET)

run: $(TARGET)
	./$(TARGET) input/1.in

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $^ -o $@

$(OBJ)/%.o: $(SRC)/%.cpp | $(OBJ)
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) -c $< -o $@

$(OBJ):
	mkdir -p $@

clean:
	rm -rv $(TARGET) $(OBJ)

