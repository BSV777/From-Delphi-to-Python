unit About;

interface

uses Windows, SysUtils, Classes, Graphics, Forms, Controls, StdCtrls,
  Buttons, ExtCtrls, shellapi;

type
  TAboutBox = class(TForm)
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    LbCop: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Shape1: TShape;
    lbExit: TLabel;
    LbURL: TLabel;
    Image2: TImage;
    lbDXR: TLabel;
    procedure FormCreate(Sender: TObject);
    procedure LbURLClick(Sender: TObject);
    procedure Image2Click(Sender: TObject);
    procedure lbDXRClick(Sender: TObject);
    procedure FormKeyDown(Sender: TObject; var Key: Word; Shift: TShiftState);
    procedure lbExitClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  AboutBox: TAboutBox;

implementation

{$R *.DFM}

procedure TAboutBox.FormCreate(Sender: TObject);
var
hsWindowRegion:Integer;
i:integer;
s:string;
const
sCop:String='436F707972696768743A2053657267657920562E4261696B6F76';
sURL:String='7365726765792E6261696B6F76406C69706574736B2E7275';
begin
hsWindowRegion:=CreateEllipticRgn(0,0,250,180);
SetWindowRgn(Handle, hsWindowRegion, True);
i:=1;
s:='';
while i<Length(sCop) do
     begin
     s:=s+Chr(StrToInt('$0'+Copy(sCop,i,2)));
     i:=i+2;
     end;
lbCop.Caption:=s;
i:=1;
s:='';
while i<Length(sURL) do
     begin
     s:=s+Chr(StrToInt('$0'+Copy(sURL,i,2)));
     i:=i+2;
     end;
lbURL.Caption:=s;
end;

procedure TAboutBox.LbURLClick(Sender: TObject);
var
TempString : array[0..79] of char;
begin
StrPCopy(TempString, 'mailto: '+LbURL.Caption);
ShellExecute(0, Nil, TempString, Nil, Nil, SW_NORMAL);
end;

procedure TAboutBox.Image2Click(Sender: TObject);
begin
Close;
end;

procedure TAboutBox.lbDXRClick(Sender: TObject);
var
TempString : array[0..79] of char;
begin
StrPCopy(TempString, LbDXR.Caption);
ShellExecute(0, Nil, TempString, Nil, Nil, SW_NORMAL);
end;

procedure TAboutBox.FormKeyDown(Sender: TObject; var Key: Word;
  Shift: TShiftState);
begin
if (Key=VK_ESCAPE) then Close;
end;

procedure TAboutBox.lbExitClick(Sender: TObject);
begin
Close;
end;

end.

