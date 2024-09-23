//scope_table.h
#include "symbol_info.h"
#include <fstream>

class scope_table {
private:
    int bucket_count;
    int unique_id;
    scope_table *parent_scope;
    vector<list<symbol_info *>> table;

    int hash_function(string name) {
        int hash = 0;
        for (char c : name) {
            hash = (hash * 31 + c) % bucket_count;
        }
        return hash;
    }

public:
    scope_table(int bucket_count, int unique_id, scope_table *parent_scope)
        : bucket_count(bucket_count), unique_id(unique_id), parent_scope(parent_scope) {
        table.resize(bucket_count);
    }

    scope_table *get_parent_scope() { return parent_scope; }
    int get_unique_id() { return unique_id; }

    symbol_info *lookup_in_scope(symbol_info* symbol) {
        int index = hash_function(symbol->get_name());
        for (auto it : table[index]) {
            if (it->get_name() == symbol->get_name()) {
                return it;
            }
        }
        return nullptr;
    }

    bool insert_in_scope(symbol_info* symbol) {
        if (lookup_in_scope(symbol) != nullptr) {
            return false;
        }
        int index = hash_function(symbol->get_name());
        table[index].push_back(symbol);
        return true;
    }

    bool delete_from_scope(symbol_info* symbol) {
        int index = hash_function(symbol->get_name());
        auto& list = table[index];
        for (auto it = list.begin(); it != list.end(); ++it) {
            if ((*it)->get_name() == symbol->get_name()) {
                list.erase(it);
                return true;
            }
        }
        return false;
    }

    void print_scope_table(ofstream& outlog) {
        outlog << "ScopeTable # " << unique_id << endl;
        for (int i = 0; i < bucket_count; ++i) {
            if (!table[i].empty()) {
                outlog << " " << i << " --> ";
                for (auto symbol : table[i]) {
                    outlog << "< " << symbol->get_name() << " : " << symbol->get_type() << " > ";
                }
                outlog << endl;
            }
        }
    }

    ~scope_table() {
        for (auto& bucket : table) {
            for (auto symbol : bucket) {
                delete symbol;
            }
        }
    }
};