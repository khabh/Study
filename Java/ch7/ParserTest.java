interface Paraseable {
    void parse (String fileName);
}

class XMLParser implements Paraseable {
    public void parse(String fileName) {
        System.out.println(fileName+"-XML parsing completed.");
    }
}

class HTMLParser implements Paraseable {
    public void parse(String fileName) {
        System.out.println(fileName+"-HTML parsing completed.");
    }
}

class ParserManager {
    public static Paraseable getParser(String type) {
        if(type.equals("XML")){
            return new XMLParser();
        }else{
            Paraseable p = new HTMLParser();
            return p;
        }
    }
}

class ParserTest {
    public static void main(String[] args) {
        // Enter Your Code Here
        Paraseable parser = ParserManager.getParser("XML");
        parser.parse("document.xml");
        parser = ParserManager.getParser("HTML");
        parser.parse("document2.html");

    }    
}
