program Editor;

uses
  Forms,
  Main in 'Main.pas' {MainForm},
  About in 'About.pas' {AboutBox},
  Parser in 'Parser.pas';

{$R *.RES}
{$R spacer.RES}

begin
Application.Initialize;
if ParamCount>1 then
     begin
     {$I-}
     AssignFile(F, ParamStr(1));
     Reset(F);
     CloseFile(F);
     {$I+}
     if IOResult=0 then
          begin
          OpenTextFile(ParamStr(1), Prop_i, Prop_s);
          WriteHTMLFile(ParamStr(2), Prop_i, Prop_s);
          end;
     end else Application.CreateForm(TMainForm, MainForm);
Application.Run;
end.
