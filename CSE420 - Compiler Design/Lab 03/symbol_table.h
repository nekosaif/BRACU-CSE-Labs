//symbol_table.h
#include "scope_table.h"

class symbol_table {
private:
    scope_table *current_scope;
    int scope_count;

public:
    symbol_table(int bucket_size) : scope_count(0) {
        current_scope = new scope_table(bucket_size, ++scope_count, nullptr);
    }

    void enter_scope(int bucket_size) {
        scope_table *new_scope = new scope_table(bucket_size, ++scope_count, current_scope);
        current_scope = new_scope;
    }

    void exit_scope() {
        if (current_scope->get_parent_scope() != nullptr) {
            scope_table *parent = current_scope->get_parent_scope();
            delete current_scope;
            current_scope = parent;
        }
    }

    bool insert(symbol_info* symbol) {
        return current_scope->insert_in_scope(symbol);
    }

    bool remove(symbol_info* symbol) {
        return current_scope->delete_from_scope(symbol);
    }

    symbol_info* lookup(symbol_info* symbol) {
        scope_table *scope = current_scope;
        while (scope != nullptr) {
            symbol_info *result = scope->lookup_in_scope(symbol);
            if (result != nullptr) {
                return result;
            }
            scope = scope->get_parent_scope();
        }
        return nullptr;
    }

    void print_current_scope_table(ofstream& outlog) {
        current_scope->print_scope_table(outlog);
    }

    void print_all_scope_tables(ofstream& outlog) {
        scope_table *scope = current_scope;
        while (scope != nullptr) {
            scope->print_scope_table(outlog);
            scope = scope->get_parent_scope();
        }
    }

    ~symbol_table() {
        while (current_scope != nullptr) {
            scope_table *parent = current_scope->get_parent_scope();
            delete current_scope;
            current_scope = parent;
        }
    }
};