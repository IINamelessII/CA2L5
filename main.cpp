#include <string>


int main(int argc, char **argv) {
    std::string s = "";

    for(int i = 1; i < argc; i++) { 
        s += " ";
        s += argv[i];
    }
    
    system(("python3 parse.py" + s).data());
    return 0;
}