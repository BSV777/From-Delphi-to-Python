#!/usr/bin/env python
# -*- coding: utf-8 -*-


# type
#   A_i=array of array of integer;
#   A_s=array of string;
#
# function OpenTextFile(PathName: string; var Prop_i:A_i; var Prop_s:A_s):boolean;
#
# const
#   MinHeight:integer=21;
#   MinWidth:integer=21;
#   DefaultHeight:integer=21;
#   DefaultWidth:integer=70;
#
# var
#   F: TextFile;
#   Prop_s:A_s; //Вектор строковых свойств объектов
#   Prop_i:A_i; //Матрица числовых свойств объектов, назначение столбцов:
#               //0 - тип объекта: Button - 1, TextEdit - 2, Label - 3
#               //1 - свойство left
#               //2 - свойство top
#               //3 - свойство width
#               //4 - свойство height
#               //5 - значение COLSPAN для ячейки HTML
#               //6 - значение ROWSPAN для ячейки HTML
#
# implementation
#
# function OpenTextFile(PathName: string; var Prop_i:A_i; var Prop_s:A_s):boolean;
# var
#   ErrFile: TextFile;
#   L,L1,LWork:string;
#   i,n:integer;
#   Errs,Valid:boolean;
# begin
# Errs:=False;
# AssignFile(F, PathName);
# Reset(F);
# i:=Pos('.', PathName);
# if i<>0 then Delete(PathName, i, Length(PathName)-i+1);
# AssignFile(ErrFile, PathName+'.log');
# Rewrite(ErrFile);
# SetLength(Prop_i, 7, 1);
# SetLength(Prop_s, 1);
# i:=1;
# while not eof(F) do
#      begin
#      ReadLn(F, L);
#      if L<>'' then
#           begin
#           LWork:=L;
#           n:=Pos('<', LWork);
#           if n=0 then LWork:='<'+LWork else Delete(LWork, 1, n-1);
#           n:=Pos('>', LWork);
#           if n=0 then LWork:=LWork+'>' else LWork:=Copy(LWork, 1, n);
#           repeat
#                n:=Pos('  ', LWork);
#                if n<>0 then Delete(LWork, n, 1);
#           until n=0;
#           n:=Pos('< ', LWork);
#           if n<>0 then Delete(LWork, n+1, 1);
#           SetLength(Prop_i, 7, i+1);
#           SetLength(Prop_s, i+1);
#           if Pos('<button', LowerCase(LWork))<>0 then Prop_i[0, i]:=1;
#           if Pos('<textedit', LowerCase(LWork))<>0 then Prop_i[0, i]:=2;
#           if Pos('<label', LowerCase(LWork))<>0 then Prop_i[0, i]:=3;
#           if Prop_i[0, i]<>0 then
#                begin
#                repeat
#                     n:=Pos(' ', LWork);
#                     if n<>0 then Delete(LWork, n, 1);
#                until n=0;
#                n:=Pos('left="', LowerCase(LWork));
#                if n<>0 then
#                     begin
#                     L1:=LWork;
#                     Delete(L1, 1, Pos('left="', LowerCase(L1))+5);
#                     L1:=Copy(L1, 1, Pos('"', L1)-1);
#                          try Prop_i[1, i]:=StrToInt(L1);
#                          except on E: EConvertError do Prop_i[1, i]:=0;
#                          end;
#                     end;
#                n:=Pos('top="', LowerCase(LWork));
#                if n<>0 then
#                     begin
#                     L1:=LWork;
#                     Delete(L1, 1, Pos('top="', LowerCase(L1))+4);
#                     L1:=Copy(L1, 1, Pos('"', L1)-1);
#                          try Prop_i[2, i]:=StrToInt(L1);
#                          except on E: EConvertError do Prop_i[2, i]:=0;
#                          end;
#                     end;
#                n:=Pos('width="', LowerCase(LWork));
#                if n<>0 then
#                     begin
#                     L1:=LWork;
#                     Delete(L1, 1, Pos('width="', LowerCase(L1))+6);
#                     L1:=Copy(L1, 1, Pos('"', L1)-1);
#                          try Prop_i[3, i]:=StrToInt(L1);
#                          except on E: EConvertError do Prop_i[3, i]:=0;
#                          end;
#                     end;
#                if Prop_i[0, i]<>2 then
#                     begin
#                     n:=Pos('height="', LowerCase(LWork));
#                     if n<>0 then
#                          begin
#                          L1:=LWork;
#                          Delete(L1, 1, Pos('height="', LowerCase(L1))+7);
#                          L1:=Copy(L1, 1, Pos('"', L1)-1);
#                          try Prop_i[4, i]:=StrToInt(L1);
#                          except on E: EConvertError do Prop_i[4, i]:=0;
#                          end;
#                          end;
#                     end;
#                n:=Pos('caption="', LowerCase(LWork));
#                if n<>0 then
#                     begin
#                     L1:=L;
#                     Delete(L1, 1, Pos('caption', LowerCase(L1))+6);
#                     Delete(L1, 1, Pos('"', L1));
#                     L1:=Copy(L1, 1, Pos('"', L1)-1);
#                     Prop_s[i]:=L1;
#                     end;
#                n:=Pos('text="', LowerCase(LWork));
#                if n<>0 then
#                     begin
#                     L1:=L;
#                     n:=Pos('textedit', LowerCase(L1));
#                     if n<>0 then Delete(L1, 1, n+7);
#                     Delete(L1, 1, Pos('text', LowerCase(L1))+3);
#                     Delete(L1, 1, Pos('"', L1));
#                     L1:=Copy(L1, 1, Pos('"', L1)-1);
#                     Prop_s[i]:=L1;
#                     end;
#                if Prop_i[1, i]<0 then Prop_i[1, i]:=0;
#                if Prop_i[2, i]<0 then Prop_i[2, i]:=0;
#                if Prop_i[3, i]<MinWidth then Prop_i[3, i]:=DefaultWidth;
#                if Prop_i[4, i]<MinHeight then Prop_i[4, i]:=DefaultHeight;
#                if Prop_i[0, i]=2 then Prop_i[4, i]:=MinHeight;
#                Valid:=True;
#                if i>1 then
#                     begin
#                     n:=1;
#                          repeat
#                          if (Prop_i[2, i]+Prop_i[4, i]>Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
#                             (Prop_i[1, i]+Prop_i[3, i]>Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
#                          n:=n+1;
#                          until (Valid=False)or(n=i);
#                     end;
#                if not Valid then //Попытка коррекции объекта перемещением
#                     begin
#                     Valid:=True;
#                     n:=1;
#                          repeat
#                          if (Prop_i[2, i]>=Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
#                          (Prop_i[1, i]>=Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
#                          n:=n+1;
#                          until (Valid=False)or(n=i);
#                     if not Valid then
#                          begin
#                          if (Prop_i[2, i]>=Prop_i[2, n-1])and(Prop_i[2, i]<Prop_i[2, n-1]+Prop_i[4, n-1])then
#                               Prop_i[2, i]:=Prop_i[2, n-1]+Prop_i[4, n-1];
#                          end;
#                     Valid:=True;
#                     n:=1;
#                          repeat
#                          if (Prop_i[2, i]>=Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
#                          (Prop_i[1, i]>=Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
#                          n:=n+1;
#                          until (Valid=False)or(n=i);
#                     if not Valid then
#                          begin
#                          if (Prop_i[1, i]>=Prop_i[1, n-1])and(Prop_i[1, i]<Prop_i[1, n-1]+Prop_i[3, n-1])then
#                               Prop_i[1, i]:=Prop_i[1, n-1]+Prop_i[3, n-1];
#                          end;
#                     Valid:=True;
#                     n:=1;
#                          repeat
#                          if (Prop_i[2, i]+Prop_i[4, i]>Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
#                             (Prop_i[1, i]+Prop_i[3, i]>Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
#                          n:=n+1;
#                          until (Valid=False)or(n=i);
#                     end;
#                if not Valid then //Попытка коррекции объекта уменьшением
#                     begin
#                     Prop_i[3, i]:=MinWidth;
#                     Prop_i[4, i]:=MinHeight;
#                     Valid:=True;
#                     n:=1;
#                          repeat
#                          if (Prop_i[2, i]+Prop_i[4, i]>Prop_i[2, n])and(Prop_i[2, i]<Prop_i[2, n]+Prop_i[4, n])and
#                             (Prop_i[1, i]+Prop_i[3, i]>Prop_i[1, n])and(Prop_i[1, i]<Prop_i[1, n]+Prop_i[3, n])then Valid:=False;
#                          n:=n+1;
#                          until (Valid=False)or(n=i);
#                     end;
#                if Valid then i:=i+1 else
#                     begin
#                     SetLength(Prop_i, 7, i);
#                     SetLength(Prop_s, i);
#                     Writeln(ErrFile, L+' - строка отвергнута: значительное наложение объектов.');
#                     Errs:=True;
#                     end;
#                end
#                else
#                begin
#                SetLength(Prop_i, 7, i);
#                SetLength(Prop_s, i);
#                Writeln(ErrFile, L+' - строка отвергнута: неверный тип объекта.');
#                Errs:=True;
#                end;
#           end;
#      end;
# CloseFile(F);
# CloseFile(ErrFile);
# if not Errs then DeleteFile(PathName+'.log');
# Result:=Errs;
