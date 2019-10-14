class Solution {
    public String convert(String s, int numRows) {
        
        if (numRows==1){
            return s;
        }
        char[][] map=new char[numRows][s.length()];
        //  初始化
        for(int i=0;i<numRows;i++){
            for(int j=0;j<s.length();j++){
                map[i][j]=' ';
            }
        }
        int flag=0;int column;
        char[] ans = new char[s.length()];
        int converse=0;
        for( column=0;;){
            for(int row=0;;){
                if(flag<s.length()){
                    if((column)%(numRows-1)==0){
                        map[row][column]=s.charAt(flag++);
                        if(row==numRows-1){
                            converse=1;
                            column++;
                        }
                        if(row==0&&column!=0){
                            converse=0;
                            column++;
                        }
                        if(converse==0) {
                            row++;
                        }else {
                            row--;
                        }
                    }else{
                        map[row][column]=s.charAt(flag++);
                        column++;
                        if(converse==0) {
                            row++;
                        }else {
                            row--;
                        }
                    }
                }else {
                    int count=0;
                    for(int i=0;i<numRows;i++){
                        for(int j=0;j<=column;j++){
                            if(map[i][j]!=' '&&count<s.length()){
                                ans[count++]=map[i][j];
                            }
                        }
                    }
                    String answer=new String(ans);
                    return answer;
                }
            }
        }
    }
}