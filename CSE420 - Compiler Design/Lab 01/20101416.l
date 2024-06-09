%option noyywrap

%{
#include<bits/stdc++.h>
using namespace std;

ofstream yyoutlog; //output filestream for log file

string loglist = ""; //list of tokens along with line numbers

// define necessary c++ variables and functions here (if any)
int lines = 1;

map<std::string, std::string> symbol_token_map = {
    {"+", "ADDOP"},
    {"-", "ADDOP"},
    {"*", "MULOP"},
    {"/", "MULOP"},
    {"%", "MULOP"},
    {"++", "INCOP"},
    {"--", "INCOP"},
    {"<", "RELOP"},
    {">", "RELOP"},
    {"==", "RELOP"},
    {"<=", "RELOP"},
    {">=", "RELOP"},
    {"!=", "RELOP"},
    {"=", "ASSIGNOP"},
    {"&&", "LOGICOP"},
    {"||", "LOGICOP"},
    {"!", "NOT"},
    {"(", "LPAREN"},
    {")", "RPAREN"},
    {"{", "LCURL"},
    {"}", "RCURL"},
    {"[", "LTHIRD"},
    {"]", "RTHIRD"},
    {",", "COMMA"},
    {":", "COLON"},
    {";", "SEMICOLON"}
};

map<std::string, std::string> keyword_token_map = {
	{"if", "IF"},
	{"else", "ELSE"},
	{"for", "FOR"},
	{"while", "WHILE"},
	{"do", "DO"},
	{"break", "BREAK"},
	{"int", "INT"},
	{"char", "CHAR"},
	{"float", "FLOAT"},
	{"double", "DOUBLE"},
	{"void", "VOID"},
	{"return", "RETURN"},
	{"switch", "SWITCH"},
	{"case", "CASE"},
	{"default", "DEFAULT"},
	{"continue", "CONTINUE"},
	{"goto", "GOTO"},
	{"printf", "PRINTF"}
};

%}

/* Regular Definitions */

delim	 [ \t\v\r]

/* write regular expressions for whitespace and newline */
ws	     {delim}+	 

newline  \n

letter_	 [A-Za-z_]
digit	 [0-9]

/* write regular expressions for id, float and integers */
id		 {letter_}({letter_}|{digit})*
float_reg (-?{digit}+\.{digit}+([eE][-+]?{digit}+)?)
integers_reg (-?{digit}+)


%%

{ws} { /* ignore whitespace */ }

{newline} {
			++lines;
		}

if|else|for|while|do|break|int|char|float|double|void|return|switch|case|default|continue|goto|printf {
			loglist="Line no "+to_string(lines)+": Token <"+keyword_token_map[yytext]+"> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

{integers_reg} {
			loglist="Line no "+to_string(lines)+": Token <CONST_INT> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

{float_reg} {
			loglist="Line no "+to_string(lines)+": Token <CONST_FLOAT> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


","|"+"|"-"|"*"|"/"|"%"|"++"|"--"|"<"|">"|"=="|"<="|">="|"!="|"="|"&&"|"||"|"!"|"("|")"|"{"|"}"|"["|"]"|","|":"|";" {
			loglist="Line no "+to_string(lines)+": Token <"+symbol_token_map[yytext]+"> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}

{id} {
			loglist="Line no "+to_string(lines)+": Token <ID> Lexeme "+yytext+" found"+"\n"+"\n";
			yyoutlog<<loglist;
		}


%%

int main(int argc, char *argv[])
{

	if(argc != 2) //check if file name is given
	{
		cout<<"Please input file name"<<endl;
		return 0;
	}

	yyin = fopen(argv[1], "r"); //the file to be read must be assigned to yyin

	yyoutlog.open("20101416_log.txt", ios::trunc); // remember to rename the log file as mentioned in the spec
	
	if(yyin == NULL) // file does not exist
	{
		// print error message and exit
		cout<<"File does not exist"<<endl;
	}
	
	yylex(); // start reading the input file in a loop
	
	//print total number of lines found in the input file
	loglist = "\nTotal lines: " + to_string(lines);
	yyoutlog << loglist;

	
	yyoutlog.close();  // close the log file
	
	fclose(yyin); // close the input file
}