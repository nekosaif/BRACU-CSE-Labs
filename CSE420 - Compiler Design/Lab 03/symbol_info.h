//symbol_info.h
#include <bits/stdc++.h>
using namespace std;

class symbol_info {
private:
    string name;
    string type;
    string symbol_type; // variable/array/function
    string data_type; // int/float/void/...
    vector<string> parameters; // for functions
    vector<string> param_types;
    int array_size; // for arrays

public:
    symbol_info(string name, string type) : name(name), type(type), array_size(0) {}

    string get_name() { return name; }
    string get_type() { return type; }
    void set_name(string name) { this->name = name; }
    void set_type(string type) { this->type = type; }

    void set_symbol_type(string st) { symbol_type = st; }
    string get_symbol_type() { return symbol_type; }

    void set_data_type(string dt) { data_type = dt; }
    string get_data_type() { return data_type; }

    void add_parameter(string param) { parameters.push_back(param); }
    vector<string> get_parameters() { return parameters; }

    void add_param_type(string type) { param_types.push_back(type); }

    void set_array_size(int size) { array_size = size; }
    int get_array_size() { return array_size; }

    ~symbol_info() {}
};