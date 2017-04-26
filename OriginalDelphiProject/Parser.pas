unit Parser;

interface

uses SysUtils, Classes;

type
  A_i=array of array of integer;
  A_s=array of string;

function OpenTextFile(PathName: string; var Prop_i:A_i; var Prop_s:A_s):boolean;
procedure WriteHTMLFile(PathName: string; var Prop_i:A_i; var Prop_s:A_s);

const
  MinHeight:integer=21;
  MinWidth:integer=21;
  DefaultHeight:integer=21;
  DefaultWidth:integer=70;

var
  F: TextFile;
  Prop_s:A_s; //������ ��������� ������� ��������
  Prop_i:A_i; //������� �������� ������� ��������, ���������� ��������:
              //0 - ��� �������: Button - 1, TextEdit - 2, Label - 3
              //1 - �������� left
              //2 - �������� top
              //3 - �������� width
              //4 - �������� height
              //5 - �������� COLSPAN ��� ������ HTML
              //6 - �������� ROWSPAN ��� ������ HTML

implementation

function OpenTextFile(PathName: string; var Prop_i:A_i; var Prop_s:A_s):boolean;
var
  ErrFile: TextFile;
  L,L1,LWork:string;
  i,n:integer;
  Errs,Valid:boolean;
begin
Errs:=False;
AssignFile(F, PathName);
Reset(F);
i:=Pos('.', PathName);
if i<>0 then Delete(PathName, i, Length(PathName)-i+1);
AssignFile(ErrFile, PathName+'.log');
Rewrite(ErrFile);
SetLength(Prop_i, 7, 1);
SetLength(Prop_s, 1);
i:=1;
while not eof(F) do
     begin
     ReadLn(F, L);
     if L<>'' then
          begin
          LWork:=L;
          n:=Pos('<', LWork);
          if n=0 then LWork:='<'+LWork else Delete(LWork, 1, n-1);
          n:=Pos('>', LWork);
          if n=0 then LWork:=LWork+'>' else LWork:=Copy(LWork, 1, n);
          repeat
               n:=Pos('  ', LWork);
               if n<>0 then Delete(LWork, n, 1);
          until n=0;
          n:=Pos('< ', LWork);
          if n<>0 then Delete(LWork, n+1, 1);
          SetLength(Prop_i, 7, i+1);
          SetLength(Prop_s, i+1);
          if Pos('<button', LowerCase(LWork))<>0 then Prop_i[0, i]:=1;
          if Pos('<textedit', LowerCase(LWork))<>0 then Prop_i[0, i]:=2;
          if Pos('<label', LowerCase(LWork))<>0 then Prop_i[0, i]:=3;
          if Prop_i[0, i]<>0 then
               begin
               repeat
                    n:=Pos(' ', LWork);
                    if n<>0 then Delete(LWork, n, 1);
               until n=0;
               n:=Pos('left="', LowerCase(LWork));
               if n<>0 then
                    begin
                    L1:=LWork;
                    Delete(L1, 1, Pos('left="', LowerCase(L1))+5);
                    L1:=Copy(L1, 1, Pos('"', L1)-1);
                         try Prop_i[1, i]:=StrToInt(L1);
                         except on E: EConvertError do Prop_i[1, i]:=0;
                         end;
                    end;
               n:=Pos('top="', LowerCase(LWork));
               if n<>0 then
                    begin
                    L1:=LWork;
                    Delete(L1, 1, Pos('top="', LowerCase(L1))+4);
                    L1:=Copy(L1, 1, Pos('"', L1)-1);
                         try Prop_i[2, i]:=StrToInt(L1);
                         except on E: EConvertError do Prop_i[2, i]:=0;
                         end;
                    end;
               n:=Pos('width="', LowerCase(LWork));
               if n<>0 then
                    begin
                    L1:=LWork;
                    Delete(L1, 1, Pos('width="', LowerCase(L1))+6);
                    L1:=Copy(L1, 1, Pos('"', L1)-1);
                         try Prop_i[3, i]:=StrToInt(L1);
                         except on E: EConvertError do Prop_i[3, i]:=0;
                         end;
                    end;
               if Prop_i[0, i]<>2 then
                    begin
                    n:=Pos('height="', LowerCase(LWork));
                    if n<>0 then
                         begin
                         L1:=LWork;
                         Delete(L1, 1, Pos('height="', LowerCase(L1))+7);
                         L1:=Copy(L1, 1, Pos('"', L1)-1);
                         try Prop_i[4, i]:=StrToInt(L1);
                         except on E: EConvertError do Prop_i[4, i]:=0;
                         end;
                         end;
                    end;
               n:=Pos('caption="', LowerCase(LWork));
               if n<>0 then
                    begin
                    L1:=L;
                    Delete(L1, 1, Pos('caption', LowerCase(L1))+6);
                    Delete(L1, 1, Pos('"', L1));
                    L1:=Copy(L1, 1, Pos('"', L1)-1);
                    Prop_s[i]:=L1;
                    end;
               n:=Pos('text="', LowerCase(LWork));
               if n<>0 then
                    begin
                    L1:=L;
                    n:=Pos('textedit', LowerCase(L1));
                    if n<>0 then Delete(L1, 1, n+7);
                    Delete(L1, 1, Pos('text', LowerCase(L1))+3);
                    Delete(L1, 1, Pos('"', L1));
                    L1:=Copy(L1, 1, Pos('"', L1)-1);
                    Prop_s[i]:=L1;
                    end;
               if Prop_i[1, i]<0 then Prop_i[1, i]:=0;
               if Prop_i[2, i]<0 then Prop_i[2, i]:=0;
               if Prop_i[3, i]<MinWidth then Prop_i[3, i]:=DefaultWidth;
               if Prop_i[4, i]<MinHeight then Prop_i[4, i]:=DefaultHeight;
               if Prop_i[0, i]=2 then Prop_i[4, i]:=MinHeight;
               Valid:=True;
               if i>1 then
                    begin
                    n:=1;
                         repeat
                         if (Prop_i[2, i]+Prop_i[4, i]>Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
                            (Prop_i[1, i]+Prop_i[3, i]>Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
                         n:=n+1;
                         until (Valid=False)or(n=i);
                    end;
               if not Valid then //������� ��������� ������� ������������
                    begin
                    Valid:=True;
                    n:=1;
                         repeat
                         if (Prop_i[2, i]>=Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
                         (Prop_i[1, i]>=Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
                         n:=n+1;
                         until (Valid=False)or(n=i);
                    if not Valid then
                         begin
                         if (Prop_i[2, i]>=Prop_i[2, n-1])and(Prop_i[2, i]<Prop_i[2, n-1]+Prop_i[4, n-1])then
                              Prop_i[2, i]:=Prop_i[2, n-1]+Prop_i[4, n-1];
                         end;
                    Valid:=True;
                    n:=1;
                         repeat
                         if (Prop_i[2, i]>=Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
                         (Prop_i[1, i]>=Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
                         n:=n+1;
                         until (Valid=False)or(n=i);
                    if not Valid then
                         begin
                         if (Prop_i[1, i]>=Prop_i[1, n-1])and(Prop_i[1, i]<Prop_i[1, n-1]+Prop_i[3, n-1])then
                              Prop_i[1, i]:=Prop_i[1, n-1]+Prop_i[3, n-1];
                         end;
                    Valid:=True;
                    n:=1;
                         repeat
                         if (Prop_i[2, i]+Prop_i[4, i]>Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
                            (Prop_i[1, i]+Prop_i[3, i]>Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
                         n:=n+1;
                         until (Valid=False)or(n=i);
                    end;
               if not Valid then //������� ��������� ������� �����������
                    begin
                    Prop_i[3, i]:=MinWidth;
                    Prop_i[4, i]:=MinHeight;
                    Valid:=True;
                    n:=1;
                         repeat
                         if (Prop_i[2, i]+Prop_i[4, i]>Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
                            (Prop_i[1, i]+Prop_i[3, i]>Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
                         n:=n+1;
                         until (Valid=False)or(n=i);
                    end;
               if Valid then i:=i+1 else
                    begin
                    SetLength(Prop_i, 7, i);
                    SetLength(Prop_s, i);
                    Writeln(ErrFile, L+' - ������ ����������: ������������ ��������� ��������.');
                    Errs:=True;
                    end;
               end
               else
               begin
               SetLength(Prop_i, 7, i);
               SetLength(Prop_s, i);
               Writeln(ErrFile, L+' - ������ ����������: �������� ��� �������.');
               Errs:=True;
               end;
          end;
     end;
CloseFile(F);
CloseFile(ErrFile);
if not Errs then DeleteFile(PathName+'.log');
Result:=Errs;
end;

procedure WriteHTMLFile(PathName: string; var Prop_i:A_i; var Prop_s:A_s);
var
  Res:TResourceStream;
  NCom,NX,NY,i,j,n,x,y,k,p,t:integer;
  F: TextFile;
  s,ts,L:string;
  sp:boolean;
  Matr: array of array of integer; //������� ������� �������, ���
                                   //������ 0 - ���������� ���������� ������������ ������ ��������
                                   //������� 0 - ���������� ���������� �������������� ������ ��������
                                   //��������� �������� ����� ������:
                                   //32767 - �������������� ������
                                   //N > 0 - ������ �������� ����� ������� ���� ������� N
                                   //M < 0 - ������ �������� ����� ������� ���� ������� ����� M
                                   //0 - ��� ��������� ������ ����� ���������

  Spc: array of array of integer;  //������� ������ ������, ���������� ��������:
                                   //0 - �������� COLSPAN ��� ������ HTML
                                   //1 - �������� ROWSPAN ��� ������ HTML
begin
NCom:=High(Prop_s);
NX:=NCom*2;
NY:=NCom*2;
SetLength(Matr, NX+1, NY+1);
for x:=0 to NX do for y:=0 to NY do Matr[x,y]:=32767;
for i:=1 to NCom do //���������� ������ 0 � ������� 0 ������������ ������ ��������
     begin
     Matr[0, i*2-1]:=Prop_i[2, i];
     Matr[0, i*2]:=Prop_i[2, i]+Prop_i[4, i];
     Matr[i*2-1, 0]:=Prop_i[1, i];
     Matr[i*2, 0]:=Prop_i[1, i]+Prop_i[3, i];
     end;
repeat //���������� �������� ������� 0
p:=0;
for k:=1 to NY-1 do
     begin
     if Matr[0, k]>Matr[0, k+1] then
          begin
          t:=Matr[0, k];
          Matr[0, k]:=Matr[0, k+1];
          Matr[0, k+1]:=t;
          p:=p+1;
          end;
     end;
until p=0;
repeat //�������� ������ � ������� 0
for k:=1 to NY-1 do
     begin
     p:=0;
     if (Matr[0, k]=Matr[0, k+1]) then
          begin
          for i:=k+1 to NY-1 do Matr[0, i]:=Matr[0, i+1];
          p:=p+1;
          end;
     end;
NY:=NY-p;
until p=0;
repeat //���������� �������� ������ 0
p:=0;
for k:=1 to NX-1 do
     begin
     if Matr[k, 0]>Matr[k+1, 0] then
          begin
          t:=Matr[k, 0];
          Matr[k, 0]:=Matr[k+1, 0];
          Matr[k+1, 0]:=t;
          p:=p+1;
          end;
     end;
until p=0;
repeat //�������� ������ � ������ 0
for k:=1 to NX-1 do
     begin
     p:=0;
     if Matr[k, 0]=Matr[k+1, 0] then
          begin
          for i:=k+1 to NX-1 do Matr[i, 0]:=Matr[i+1, 0];
          p:=p+1;
          end;
     end;
NX:=NX-p;
until p=0;
for n:=1 to NCom do //����������� �������� � ����� �����
     begin
     Prop_i[5, n]:=0;
     for x:=1 to NX do
          begin
          if (Matr[x, 0]>=Prop_i[1, n])and(Matr[x, 0]<Prop_i[1, n]+Prop_i[3, n])then
               begin
               Prop_i[5, n]:=Prop_i[5, n]+1;
               Prop_i[6, n]:=0;
               for y:=1 to NY do
               if (Matr[0, y]>=Prop_i[2, n])and(Matr[0, y]<Prop_i[2, n]+Prop_i[4, n])then
                    begin
                    Prop_i[6, n]:=Prop_i[6, n]+1;
                    if (Matr[x, 0]=Prop_i[1, n])and(Matr[0, y]=Prop_i[2, n])then
                    Matr[x, y]:=n else Matr[x, y]:=0;
                    end;
               end;
          end;
     end;
n:=1; //����������� ������ ����� � �����
for y:=1 to NY-1 do
     begin
     for x:=1 to NX-1 do
          begin
          i:=1;
          if Matr[x, y]=32767 then
               begin
               Matr[x, y]:=-n;
               while (Matr[x+i, y]=32767)and(x+i<NX) do
                    begin
                    Matr[x+i, y]:=0;
                    i:=i+1;
                    end;
               j:=1;
               sp:=True;
               while (sp=True)and(y+j<NY)do
                    begin
                    sp:=True;
                    for k:=x to x+i-1 do if Matr[k, y+j]<>32767 then sp:=False;
                    if sp=True then
                         begin
                         for k:=x to x+i-1 do Matr[k, y+j]:=0;
                         j:=j+1;
                         end;
                    end;
               SetLength(Spc, 2, n+1);
               Spc[0, n]:=i;
               Spc[1, n]:=j;
               n:=n+1;
               end;
          end;
     end;
i:=Pos('.', PathName);
if i=0 then PathName:=PathName+'.htm';
AssignFile(F, PathName);
Rewrite(F);
Writeln(F, '<HTML>');
Writeln(F, '<HEAD>');
Writeln(F, '<TITLE>���������� ������� - Sergey V.Baikov - sergey.baikov@lipetsk.ru</TITLE>');
Writeln(F, '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1251">');
Writeln(F, '</HEAD>');
Writeln(F, '<BODY BGCOLOR=#ffffff>');
Writeln(F, '<FORM>');
Writeln(F, '<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH='+IntToStr(Matr[NX, 0]-Matr[1, 0])+'>');
Writeln(F, '   <TR>');
for i:=1 to NX-1 do
     begin
     s:='      <TD><IMG height=1 src="spacer.gif" width='+
     IntToStr(Matr[i+1, 0]-Matr[i, 0])+'></TD>';
     Writeln(F, s);
     end;
Writeln(F, '   </TR>');
for i:=1 to NY-1 do
     begin
     Writeln(F, '   <TR>');
     for j:=1 to NX-1 do
          begin
          if Matr[j, i]>0 then //���� �����, ���������� ������
               begin
               if Prop_i[0, Matr[j, i]]=1 then ts:='button';
               if Prop_i[0, Matr[j, i]]=2 then ts:='text';
               s:='      <TD';
               if Prop_i[5, Matr[j, i]]>1 then s:=s+' COLSPAN='+IntToStr(Prop_i[5, Matr[j, i]]);
               if Prop_i[6, Matr[j, i]]>1 then s:=s+' ROWSPAN='+IntToStr(Prop_i[6, Matr[j, i]]);
                    case Prop_i[0, Matr[j, i]] of
                    1:   begin
                         s:=s+'><INPUT HEIGHT="'+IntToStr(Prop_i[4, Matr[j, i]])+
                         '" WIDTH="'+IntToStr(Prop_i[3, Matr[j, i]])+
                         '" style="HEIGHT: '+IntToStr(Prop_i[4, Matr[j, i]])+
                         'px; WIDTH: '+IntToStr(Prop_i[3, Matr[j, i]])+
                         'px" type='+ts;
                         Writeln(F, s);
                         Writeln(F, '          value="'+Prop_s[Matr[j, i]]+'"></TD>');
                         end;
                    2:   begin
                         s:=s+'><INPUT SIZE="'+IntToStr(Prop_i[3, Matr[j, i]]div 8 -1)+
                         '" style="WIDTH: '+IntToStr(Prop_i[3, Matr[j, i]])+
                         'px" type='+ts;
                         Writeln(F, s);
                         Writeln(F, '          value="'+Prop_s[Matr[j, i]]+'"></TD>');
                         end;
                    3:   begin
                         s:=s+'>'+Prop_s[Matr[j, i]]+'</TD>';
                         Writeln(F, s);
                         end;
                    end;
               end;
          if Matr[j, i]<0 then //������ ���� �����
               begin
               s:='      <TD';
               if Spc[0, -Matr[j, i]]>1 then s:=s+' COLSPAN='+IntToStr(Spc[0, -Matr[j, i]]);
               if Spc[1, -Matr[j, i]]>1 then s:=s+' ROWSPAN='+IntToStr(Spc[1, -Matr[j, i]]);
               s:=s+'></TD>';
               Writeln(F, s);
               end;
          end;
     s:='      <TD><IMG height='+IntToStr(Matr[0, i+1]-Matr[0, i])+' src="spacer.gif" width=1></TD>';
     Writeln(F, s);
     Writeln(F, '   </TR>');
     end;
Writeln(F, '</TABLE>');
Writeln(F, '</FORM>');
Writeln(F, '</BODY>');
Writeln(F, '</HTML>');
CloseFile(F);
if not FileExists(ExtractFilePath(PathName)+'spacer.gif') then
     begin
     Res:=TResourceStream.Create(Hinstance, 'GIF', Pchar('GIFFILE'));
     Res.SavetoFile(ExtractFilePath(PathName)+'spacer.gif');
     Res.Free;
     end;
end;

end.
