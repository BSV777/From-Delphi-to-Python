unit Main;

interface

uses
  Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs,
  Menus, ExtCtrls, Buttons, StdCtrls, Grids, shellapi;

type
  TMainForm = class(TForm)
    MainMenu1: TMainMenu;
    mnF: TMenuItem;
    mnH: TMenuItem;
    mnNew: TMenuItem;
    mnOpen: TMenuItem;
    N7: TMenuItem;
    mnSave: TMenuItem;
    mnSaveAs: TMenuItem;
    mnSaveWeb: TMenuItem;
    N10: TMenuItem;
    mnExit: TMenuItem;
    mnO: TMenuItem;
    mnDel: TMenuItem;
    mnAbout: TMenuItem;
    sbSelect: TSpeedButton;
    sbCrBtn: TSpeedButton;
    sbCrTxt: TSpeedButton;
    sbCrLab: TSpeedButton;
    SgProp: TStringGrid;
    SbDesk: TScrollBox;
    STopLeft: TShape;
    STopCenter: TShape;
    STopRight: TShape;
    SMiddleLeft: TShape;
    SBottomLeft: TShape;
    SBottomCenter: TShape;
    SMiddleRight: TShape;
    SBottomRight: TShape;
    PopupMenu1: TPopupMenu;
    pmBtn: TMenuItem;
    pmTxt: TMenuItem;
    pmLab: TMenuItem;
    N19: TMenuItem;
    pmDel: TMenuItem;
    OpenDialog1: TOpenDialog;
    SaveDialog1: TSaveDialog;
    N4: TMenuItem;
    mnCrBtn: TMenuItem;
    mnCrTxt: TMenuItem;
    mnCrLab: TMenuItem;
    mnViewWeb: TMenuItem;
    N1: TMenuItem;
    procedure mnAboutClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure FormResize(Sender: TObject);
    procedure pmBtnClick(Sender: TObject);
    procedure pmTxtClick(Sender: TObject);
    procedure pmLabClick(Sender: TObject);
    procedure mnExitClick(Sender: TObject);
    procedure mnOpenClick(Sender: TObject);
    procedure mnSaveClick(Sender: TObject);
    procedure mnSaveAsClick(Sender: TObject);
    procedure mnSaveWebClick(Sender: TObject);
    procedure mnNewClick(Sender: TObject);
    procedure sbCrBtnClick(Sender: TObject);
    procedure sbCrTxtClick(Sender: TObject);
    procedure sbCrLabClick(Sender: TObject);
    procedure pmDelClick(Sender: TObject);
    procedure SgPropKeyPress(Sender: TObject; var Key: Char);
    procedure SgPropKeyDown(Sender: TObject; var Key: Word; Shift: TShiftState);
    procedure SbDeskClick(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
    procedure SgPropClick(Sender: TObject);
    procedure sbSelectClick(Sender: TObject);
    procedure SbDeskMouseDown(Sender: TObject; Button: TMouseButton; Shift: TShiftState; X, Y: Integer);
    procedure SbDeskMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure mnViewWebClick(Sender: TObject);
  private
    procedure Refresh(Sender: TObject);
    procedure PanelMouseDown(Sender: TObject; Button: TMouseButton; Shift: TShiftState; X, Y: Integer);
    procedure PanelMouseMove(Sender: TObject; Shift: TShiftState; X, Y: Integer);
    procedure ShapeMouseMove(Sender: TObject; Shift: TShiftState; X, Y: Integer);
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;
  Panel: TPanel;
  CurrentPanel, Count, CurrentShape:integer;
  PanelList:TList;

const
  X0:integer=0;
  Y0:integer=0;
  Xk:integer=0;
  Yk:integer=0;
  L0:integer=0;
  T0:integer=0;
  W0:integer=0;
  H0:integer=0;
  Lk:integer=0;
  Tk:integer=0;
  Wk:integer=0;
  Hk:integer=0;
  Modified:boolean=False;
  DefaultFileName:string='Untitled';
  CurrentFileName:string='Untitled';
  NeedCreate:integer=0;
  Valid:boolean=True;

implementation

uses About, Parser;

{$R *.DFM}

procedure TMainForm.mnAboutClick(Sender: TObject);
begin
AboutBox:=nil;
     try
     AboutBox:=TAboutBox.Create(Self);
     AboutBox.ShowModal;
     finally
     if Assigned(AboutBox) then AboutBox.Release;
     end;
end;

procedure TMainForm.FormCreate(Sender: TObject);
var i:integer;
begin
Application.ShowHint:=True;
mnCrBtn.OnClick:=sbCrBtnClick;
mnCrTxt.OnClick:=sbCrTxtClick;
mnCrLab.OnClick:=sbCrLabClick;
mnDel.OnClick:=pmDelClick;
for i:=0 to MainForm.ComponentCount-1 do if MainForm.Components[i] is TShape then
     with TShape(MainForm.Components[i]) do
     begin
     OnMouseDown:=PanelMouseDown;
     OnMouseMove:=ShapeMouseMove;
     end;
SgProp.ColWidths[0]:=40;
SgProp.Cells[0, 0]:='Left';
SgProp.ColWidths[1]:=40;
SgProp.Cells[1, 0]:='Top';
SgProp.ColWidths[2]:=40;
SgProp.Cells[2, 0]:='Width';
SgProp.ColWidths[3]:=40;
SgProp.Cells[3, 0]:='Height';
SgProp.ColWidths[4]:=129;
SgProp.Cells[4, 0]:='Caption';
PanelList:=TList.Create;
MnNewClick(Sender);
end;

procedure TMainForm.FormResize(Sender: TObject);
begin
SbDesk.Width:=Width-11;
SbDesk.Height:=Height-89;
SgProp.Width:=Width-164;
SgProp.ColWidths[4]:=Width-333;
end;

procedure TMainForm.PanelMouseMove(Sender: TObject; Shift: TShiftState; X, Y: Integer);
var i,T1,L1:integer;
begin
if (ssLeft in Shift)and((X<>X0) or (Y<>Y0)) then
     begin
     SbDeskClick(Sender);
     CurrentPanel:=(Sender as TPanel).Tag;
     Panel:=PanelList.Items[CurrentPanel];
     with Panel do
          begin
          T1:=Top;
          L1:=Left;
          Tk:=Top+Y-Y0;
          Lk:=Left+X-X0;
          end;
     with sbDesk do
          begin
          if Tk<-VertScrollBar.Position then Tk:=-VertScrollBar.Position+1;
          if Lk<-HorzScrollBar.Position then Lk:=-HorzScrollBar.Position+1;
          if Tk+Hk+VertScrollBar.Position>VertScrollBar.Range then Tk:=VertScrollBar.Range-Hk-VertScrollBar.Position-1;
          if Lk+Wk+HorzScrollBar.Position>HorzScrollBar.Range then Lk:=HorzScrollBar.Range-Wk-HorzScrollBar.Position-1;
          end;
     i:=0;
     Valid:=True;
          repeat
          if MainForm.Components[i] is TPanel then with TPanel(MainForm.Components[i]) do
          if (i<>CurrentPanel)and(Tk+Hk>Top)and(Tk<Top+Height)and(Lk+Wk>Left)and(Lk<Left+Width)then Valid:=False;
          i:=i+1;
          until (Valid=False)or(i=MainForm.ComponentCount);
     if not Valid then
          begin
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do
                         begin
                         if (T1>Top)and(L1<Left+Width)and(L1+Wk>Left)and(Tk<Top+Height) then Tk:=Top+Height;
                         if (T1<Top)and(L1<Left+Width)and(L1+Wk>Left)and(Tk+Hk>Top) then Tk:=Top-Hk;
                         if (L1>Left)and(T1+Hk>Top)and(T1<Top+Height)and(Lk<Left+Width) then Lk:=Left+Width;
                         if (L1<Left)and(T1+Hk>Top)and(T1<Top+Height)and(Lk+Wk>Left) then Lk:=Left-Wk;
                         end;
                    end;
               end;
          end;
          Refresh(Sender);
     end;
end;

procedure TMainForm.PanelMouseDown(Sender: TObject; Button: TMouseButton; Shift: TShiftState; X, Y: Integer);
begin
X0:=X;
Y0:=Y;
if Sender is TPanel then CurrentPanel:=(Sender as TPanel).Tag;
Panel:=PanelList.Items[CurrentPanel];
with Panel do
     begin
     L0:=Left;
     T0:=Top;
     H0:=Height;
     W0:=Width;;
     Lk:=Left;
     Tk:=Top;
     Hk:=Height;
     Wk:=Width;
     if BevelOuter<>bvLowered then
          begin
          STopCenter.Visible:=True;
          SBottomCenter.Visible:=True;
          end else
          begin
          STopCenter.Visible:=False;
          SBottomCenter.Visible:=False;
          end;
     if BevelOuter=bvRaised then pmBtn.Enabled:=False else pmBtn.Enabled:=True;
     if BevelOuter=bvLowered then pmTxt.Enabled:=False else pmTxt.Enabled:=True;
     if BevelOuter=bvNone then pmLab.Enabled:=False else pmLab.Enabled:=True;
     end;
STopLeft.Visible:=True;
SMiddleLeft.Visible:=True;
SBottomLeft.Visible:=True;
STopRight.Visible:=True;
SMiddleRight.Visible:=True;
SBottomRight.Visible:=True;
mnDel.Enabled:=True;
mnDel.ShortCut:= ShortCut(VK_DELETE, []);
Refresh(Sender);
end;

procedure TMainForm.ShapeMouseMove(Sender: TObject; Shift: TShiftState; X, Y: Integer);
var
  i,T1,L1,H1,W1,VX,VY,CurrentShape:integer;
begin
if ssLeft in Shift then
     begin
     VX:=X-X0;
     VY:=Y-Y0;
     CurrentShape:=(Sender as TShape).Tag;
     Panel:=PanelList.Items[CurrentPanel];
     T1:=Panel.Top;
     L1:=Panel.Left;
     H1:=Panel.Height;
     W1:=Panel.Width;
     if Panel.BevelOuter=bvLowered then VY:=0;
     case CurrentShape of
     11:  begin
          Yk:=STopLeft.Top+VY;
          Xk:=STopLeft.Left+VX;
          Tk:=Yk+3;
          if Tk< -SbDesk.VertScrollBar.Position then Tk:=-SbDesk.VertScrollBar.Position;
          Lk:=Xk+3;
          if Lk<-SbDesk.HorzScrollBar.Position then Lk:=-SbDesk.HorzScrollBar.Position;
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do
                         begin
                         if (T1>Top)and(L1<Left+Width)and(L1+Wk>Left)and(Tk<Top+Height)then Tk:=Top+Height;
                         if (L1>Left)and(T1+Hk>Top)and(T1<Top+Height)and(Lk<Left+Width) then Lk:=Left+Width;
                         end;
                    end;
               end;
          Hk:=H0+T0-Tk;
          Wk:=W0+L0-Lk;
          if Wk < MinWidth then
               begin
               Lk:=L0+W0-MinWidth;
               Wk:=MinWidth;
               end;
          if Hk < MinHeight then
               begin
               Tk:=T0+H0-MinHeight;
               Hk:=MinHeight;
               end;
          end;
     12:  begin
          Yk:=STopCenter.Top+VY;
          Tk:=Yk+3;
          if Tk< -SbDesk.VertScrollBar.Position then Tk:=-SbDesk.VertScrollBar.Position;
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do if (T1>Top)and(Lk<Left+Width)and(Lk+Wk>Left)and(Tk<Top+Height)then Tk:=Top+Height;
                    end;
               end;
          Hk:=T0+H0-Tk;
          if Hk < MinHeight then
               begin
               Tk:=T0+H0-MinHeight;
               Hk:=MinHeight;
               end;
          end;
     13:  begin
          Yk:=STopRight.Top+VY;
          Xk:=STopRight.Left+VX;
          Tk:=Yk+3;
          if Tk< -SbDesk.VertScrollBar.Position then Tk:=-SbDesk.VertScrollBar.Position;
          if Lk+Wk+SbDesk.HorzScrollBar.Position > SbDesk.HorzScrollBar.Range then
               Wk:=SbDesk.HorzScrollBar.Range-Lk-SbDesk.HorzScrollBar.Position;
          Wk:=Xk-L0+2;
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do
                         begin
                         if (Lk<Left)and(T1+Hk>Top)and(T1<Top+Height)and(Lk+Wk>Left) then Wk:=Left-Lk;
                         if (T1>Top)and(Lk<Left+Width)and(Lk+Wk>Left)and(Tk<Top+Height) then Tk:=Top+Height;
                         end;
                    end;
               end;
          Hk:=H0+T0-Tk;
          if Wk < MinWidth then Wk:=MinWidth;
          if Hk < MinHeight then
               begin
               Tk:=T0+H0-MinHeight;
               Hk:=MinHeight;
               end;
          end;
     21:  begin
          Xk:=SMiddleLeft.Left+VX;
          Lk:=Xk+3;
          if Lk<-SbDesk.HorzScrollBar.Position then Lk:=-SbDesk.HorzScrollBar.Position;
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do if (L1>Left)and(Tk+Hk>Top)and(Tk<Top+Height)and(Lk<Left+Width)then Lk:=Left+Width;
                    end;
               end;
          Wk:=W0+L0-Lk;
          if Wk < MinWidth then
               begin
               Lk:=L0+W0-MinWidth;
               Wk:=MinWidth;
               end;
          end;
     23:  begin
          Xk:=SMiddleRight.Left+VX;
          Wk:=Xk-L0+2;
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do if (Lk<Left)and(Tk+Hk>Top)and(Tk<Top+Height)and(Lk+Wk>Left) then Wk:=Left-Lk;
                    end;
               end;
          if Lk+Wk+SbDesk.HorzScrollBar.Position > SbDesk.HorzScrollBar.Range then
               Wk:=SbDesk.HorzScrollBar.Range-Lk-SbDesk.HorzScrollBar.Position;
          if Wk < MinWidth then Wk:=MinWidth;
          end;
     31:  begin
          Yk:=SBottomLeft.Top+VY;
          Xk:=SBottomLeft.Left+VX;
          Lk:=Xk+3;
          if Lk<-SbDesk.HorzScrollBar.Position then Lk:=-SbDesk.HorzScrollBar.Position;
          Hk:=Yk-T0+2;
          if Hk < MinHeight then Hk:=MinHeight;
          if Tk+Hk+SbDesk.VertScrollBar.Position > SbDesk.VertScrollBar.Range then
               Hk:=SbDesk.VertScrollBar.Range-Tk-SbDesk.VertScrollBar.Position;
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do
                         begin
                         if (Tk<Top)and(L1<Left+Width)and(L1+Wk>Left)and(Tk+Hk>Top) then Hk:=Top-Tk;
                         if (L1>Left)and(Tk+Hk>Top)and(Tk<Top+Height)and(Lk<Left+Width) then Lk:=Left+Width;
                         end;
                    end;
               end;
          Wk:=W0+L0-Lk;
          if Wk < MinWidth then
               begin
               Lk:=L0+W0-MinWidth;
               Wk:=MinWidth;
               end;
          end;
     32:  begin
          Yk:=SBottomCenter.Top+VY;
          Hk:=Yk-T0+2;
          if Tk+Hk+SbDesk.VertScrollBar.Position > SbDesk.VertScrollBar.Range then
               Hk:=SbDesk.VertScrollBar.Range-Tk-SbDesk.VertScrollBar.Position;
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do if (Tk<Top)and(Lk<Left+Width)and(Lk+Wk>Left)and(Tk+Hk>Top) then Hk:=Top-Tk;
                    end;
               end;
          if Hk < MinHeight then Hk:=MinHeight;
          end;
     33:  begin
          Yk:=SBottomRight.Top+VY;
          Xk:=SBottomRight.Left+VX;
          Hk:=Yk-T0+2;
          if Hk < MinHeight then Hk:=MinHeight;
          if Tk+Hk+SbDesk.VertScrollBar.Position > SbDesk.VertScrollBar.Range then
               Hk:=SbDesk.VertScrollBar.Range-Tk-SbDesk.VertScrollBar.Position;
          Wk:=Xk-L0+2;
          if Wk < MinWidth then Wk:=MinWidth;
          if Lk+Wk+SbDesk.HorzScrollBar.Position > SbDesk.HorzScrollBar.Range then
               Wk:=SbDesk.HorzScrollBar.Range-Lk-SbDesk.HorzScrollBar.Position;
          Count:=PanelList.Count-1;
          for i:=0 to Count do
               begin
               if i<>CurrentPanel then
                    begin
                    Panel:=PanelList.Items[i];
                    with Panel do
                         begin
                         if (Lk<Left)and(Tk+H1>Top)and(Tk<Top+Height)and(Lk+Wk>Left) then Wk:=Left-Lk;
                         if (Tk<Top)and(Lk<Left+Width)and(Lk+W1>Left)and(Tk+Hk>Top) then Hk:=Top-Tk;
                         end;
                    end;
               end;
          end;
     end;
     Refresh(Sender);
     end;
end;

procedure TMainForm.pmBtnClick(Sender: TObject);
begin
Panel:=PanelList.Items[CurrentPanel];
Panel.BevelOuter:=bvRaised;
Panel.Color:=clBtnFace;
Panel.Alignment:=taCenter;
SgProp.Cells[4, 0]:='Caption';
STopCenter.Visible:=True;
SBottomCenter.Visible:=True;
Refresh(Sender);
end;

procedure TMainForm.pmTxtClick(Sender: TObject);
begin
Panel:=PanelList.Items[CurrentPanel];
Panel.BevelOuter:=bvLowered;
Panel.Color:=clHighlightText;
Panel.Alignment:=taLeftJustify;
Hk:=MinHeight;
SgProp.Cells[4, 0]:='Text';
STopCenter.Visible:=False;
SBottomCenter.Visible:=False;
Refresh(Sender);
end;

procedure TMainForm.pmLabClick(Sender: TObject);
begin
Panel:=PanelList.Items[CurrentPanel];
Panel.BevelOuter:=bvNone;
Panel.Color:=clBtnFace;
Panel.Alignment:=taLeftJustify;
SgProp.Cells[4, 0]:='Text';
Refresh(Sender);
end;

procedure TMainForm.Refresh(Sender: TObject);
begin
Modified := True;
Panel:=PanelList.Items[CurrentPanel];
with Panel do
     begin
     if BevelOuter=bvRaised then SgProp.Cells[4, 0]:='Caption';
     if (BevelOuter=bvLowered)or(BevelOuter=bvNone) then SgProp.Cells[4, 0]:='Text';
     Top:=Tk;
     Height:=Hk;
     Left:=Lk;
     Width:=Wk;
     SgProp.Cells[0, 1]:=IntToStr(Left+SbDesk.HorzScrollBar.Position);
     SgProp.Cells[1, 1]:=IntToStr(Top+SbDesk.VertScrollBar.Position);
     SgProp.Cells[2, 1]:=IntToStr(Width);
     SgProp.Cells[3, 1]:=IntToStr(Height);
     SgProp.Cells[4, 1]:=Caption;
     STopLeft.Top:=Top-3;
     STopLeft.Left:=Left-3;
     STopCenter.Top:=Top-3;
     STopCenter.Left:=Left+Width div 2 - 2;
     STopRight.Top:=Top-3;
     STopRight.Left:=Left+Width-2;
     SMiddleLeft.Top:=Top+Height div 2 -2;
     SMiddleLeft.Left:=Left-3;
     SMiddleRight.Top:=Top+Height div 2 -2;
     SMiddleRight.Left:=Left+Width-2;
     SBottomLeft.Top:=Top+Height-2;
     SBottomLeft.Left:=Left-3;
     SBottomCenter.Top:=Top+Height-2;
     SBottomCenter.Left:=Left+Width div 2 - 2;
     SBottomRight.Top:=Top+Height-2;
     SBottomRight.Left:=Left+Width-2;
     end;
end;

procedure TMainForm.mnExitClick(Sender: TObject);
begin
Close;
end;

procedure TMainForm.mnOpenClick(Sender: TObject);
var
  DialogValue,i:integer;
  TempString:array[0..79] of char;
  LogName:string;
begin
if Modified then
     begin
     DialogValue:=MessageDlg('��������� ��������� � �����?', mtWarning, [mbYes, mbNo], 0);
     if DialogValue=mrYes then mnSaveClick(Sender);
     end;
if OpenDialog1.Execute then
     begin
     CurrentFileName:=OpenDialog1.FileName;
     {$I-}
     AssignFile(F, CurrentFileName);
     Reset(F);
     CloseFile(F);
     {$I+}
     if IOResult=0 then
          begin
          Count:=PanelList.Count-1;
          for i:=Count downto 0 do
               begin
               Panel:=PanelList.Items[i];
               PanelList.Delete(i);
               Panel.Free;
               end;
          if OpenTextFile(CurrentFileName, Prop_i, Prop_s) then
               begin
               LogName:=Copy(ExtractFileName(CurrentFileName),1,Length(ExtractFileName(CurrentFileName))-4)+'.log';
               DialogValue:=MessageDlg('� ������������ ���������� ������.'+Chr(13)+Chr(10)+'����������� � �������: '+
               LogName+Chr(13)+Chr(10)+'������� '+LogName+' ?', mtWarning, [mbYes, mbNo], 0);
               if DialogValue=mrYes then
                    begin
                    StrPCopy(TempString, LogName);
                    ShellExecute(0, Nil, TempString, Nil, Nil, SW_NORMAL);
                    end;
               end;
          for i:=1 to High(Prop_s) do
               begin
               PanelList.Add(TPanel.Create(Self));
               Count:=PanelList.Count-1;
               Panel:=PanelList.Items[Count];
               with Panel do
                    begin
                    Parent:=SbDesk;
                         case Prop_i[0, i] of
                         1:   begin
                              BevelOuter:=bvRaised;
                              Color:=clBtnFace;
                              Alignment:=taCenter;
                              end;
                         2:   begin
                              BevelOuter:=bvLowered;
                              Color:=clHighlightText;
                              Alignment:=taLeftJustify;
                              end;
                         3:   begin
                              BevelOuter:=bvNone;
                              Color:=clBtnFace;
                              Alignment:=taLeftJustify;
                              end;
                         end;
                    Tag:=Count;
                    Cursor:=crSizeAll;
                    BevelWidth:=2;
                    Caption:=Prop_s[i];
                    TabOrder:=0;
                    PopupMenu:=PopupMenu1;
                    OnMouseDown:=PanelMouseDown;
                    OnMouseMove:=PanelMouseMove;
                    end;
               Lk:=Prop_i[1, i]-sbDesk.HorzScrollBar.Position;
               Tk:=Prop_i[2, i]-sbDesk.VertScrollBar.Position;
               Wk:=Prop_i[3, i];
               Hk:=Prop_i[4, i];
               CurrentPanel:=Count;
               Refresh(Sender);
               end;
          Caption:='Editor - '+ExtractFileName(CurrentFileName);
          Modified := False;
          SbDeskClick(Sender);
          end;
     end;
end;

procedure TMainForm.mnSaveClick(Sender: TObject);
var
  i,p,t:integer;
  ObjectType, TextProp:string;
  Sort:array of array of integer;
begin
Modified := False;
if CurrentFileName=DefaultFileName then MnSaveAsClick(Sender) else
     begin
     Count:=PanelList.Count-1;
     SetLength(Sort, 3, Count+1);
     for i:=0 to Count do //���������� ������� ��� ���������� Top, Left
          begin
          Sort[0,i]:=i;
          Panel:=PanelList.Items[i];
          Sort[1,i]:=Panel.Left;
          Sort[2,i]:=Panel.Top;
          end;
     repeat //���������� �� ��������� Left
     p:=0;
     for i:=0 to Count-1 do
          begin
          if Sort[1, i]>Sort[1, i+1] then
               begin
               t:=Sort[0, i];
               Sort[0, i]:=Sort[0, i+1];
               Sort[0, i+1]:=t;
               t:=Sort[1, i];
               Sort[1, i]:=Sort[1, i+1];
               Sort[1, i+1]:=t;
               t:=Sort[2, i];
               Sort[2, i]:=Sort[2, i+1];
               Sort[2, i+1]:=t;
               p:=p+1;
               end;
          end;
     until p=0;
     repeat //���������� �� ��������� Top
     p:=0;
     for i:=0 to Count-1 do
          begin
          if Sort[2, i]>Sort[2, i+1] then
               begin
               t:=Sort[0, i];
               Sort[0, i]:=Sort[0, i+1];
               Sort[0, i+1]:=t;
               t:=Sort[1, i];
               Sort[1, i]:=Sort[1, i+1];
               Sort[1, i+1]:=t;
               t:=Sort[2, i];
               Sort[2, i]:=Sort[2, i+1];
               Sort[2, i+1]:=t;
               p:=p+1;
               end;
          end;
     until p=0;
     AssignFile(F, CurrentFileName);
     Rewrite(F);
     for i:=0 to Count do
          begin
          Panel:=PanelList.Items[Sort[0,i]];
          with Panel do
               begin
               if BevelOuter=bvRaised then ObjectType:='Button';
               if BevelOuter=bvLowered then ObjectType:='TextEdit';
               if BevelOuter=bvNone then ObjectType:='Label';
               if ObjectType='Button' then TextProp:='caption' else TextProp:='text';
               Write(F, '<'+ObjectType);
               Write(F, ' left="'+IntToStr(Left+sbDesk.HorzScrollBar.Position)+'";');
               Write(F, ' top="'+IntToStr(Top+sbDesk.VertScrollBar.Position)+'";');
               Write(F, ' width="'+IntToStr(Width)+'";');
               if ObjectType<>'TextEdit' then Write(F, ' height="'+IntToStr(Height)+'";');
               Writeln(F, ' '+TextProp+'="'+Caption+'">');
               end;
          end;
     CloseFile(F);
     end;
end;

procedure TMainForm.mnSaveAsClick(Sender: TObject);
var
  DialogValue, i:integer;
  FileName:string;
begin
FileName:=CurrentFileName;
i:=Pos('.', FileName);
if i<>0 then Delete(FileName, i, Length(FileName)-i+1);
FileName:=FileName+'.txt';
SaveDialog1.FileName := FileName;
SaveDialog1.Filter:='Text files (*.txt)|*.txt|All files|*.*';
if SaveDialog1.Execute then
     begin
     FileName:=SaveDialog1.FileName;
     i:=Pos('.', FileName);
     if i=0 then FileName:=FileName+'.txt';
     DialogValue:=mrYes;
     if FileExists(FileName)then DialogValue:=MessageDlg('���� '+ExtractFileName(FileName)+' ����������. ������������?', mtWarning, [mbYes, mbNo], 0);
     if DialogValue=mrYes then
          begin
          CurrentFileName:=FileName;
          Caption:='Editor - '+ExtractFileName(CurrentFileName);
          MnSaveClick(Sender);
          end;
     end;
end;

procedure TMainForm.mnSaveWebClick(Sender: TObject);
var
  DialogValue,i,j:integer;
  HTMLFileName:string;
begin
j:=1;
SetLength(Prop_i, 7, 1);
SetLength(Prop_s, 1);
for i:=0 to MainForm.ComponentCount-1 do if MainForm.Components[i] is TPanel then
     with TPanel(MainForm.Components[i]) do
     begin
     SetLength(Prop_i, 7, j+1);
     SetLength(Prop_s, j+1);
     if BevelOuter=bvRaised then Prop_i[0, j]:=1;
     if BevelOuter=bvLowered then Prop_i[0, j]:=2;
     if BevelOuter=bvNone then Prop_i[0, j]:=3;
     Prop_i[1, j]:=Left+sbDesk.HorzScrollBar.Position;
     Prop_i[2, j]:=Top+sbDesk.VertScrollBar.Position;
     Prop_i[3, j]:=Width;
     Prop_i[4, j]:=Height;
     Prop_s[j]:=Caption;
     j:=j+1;
     end;
if j>1 then
     begin
     HTMLFileName:=CurrentFileName;
     i:=Pos('.', HTMLFileName);
     if i<>0 then Delete(HTMLFileName, i, Length(HTMLFileName)-i+1);
     SaveDialog1.FileName:= HTMLFileName+'.htm';
     SaveDialog1.Filter:='HTML files (*.htm; *.html)|*.htm; *.html|All files|*.*';
     if SaveDialog1.Execute then
          begin
          HTMLFileName:=SaveDialog1.FileName;
          DialogValue:=mrYes;
          if FileExists(HTMLFileName)then DialogValue:=MessageDlg('���� '+ExtractFileName(HTMLFileName)+' ����������. ������������?', mtWarning, [mbYes, mbNo], 0);
          if DialogValue=mrYes then WriteHTMLFile(HTMLFileName, Prop_i, Prop_s);
          end;
     end;
end;

procedure TMainForm.mnNewClick(Sender: TObject);
var
  DialogValue, i:integer;
begin
if Modified then
     begin
     DialogValue:=MessageDlg('��������� ��������� � �����?', mtWarning, [mbYes, mbNo], 0);
     if DialogValue=mrYes then mnSaveClick(Sender);
     end;
Modified:=False;
CurrentFileName:=DefaultFileName;
Caption:='Editor - '+ExtractFileName(CurrentFileName);
Count:=PanelList.Count-1;
for i:=Count downto 0 do
     begin
     Panel:=PanelList.Items[i];
     PanelList.Delete(i);
     Panel.Free;
     end;
SbDeskClick(Sender);
end;

procedure TMainForm.sbCrBtnClick(Sender: TObject);
begin
sbCrBtn.Down:=True;
NeedCreate:=1;
sbDesk.Cursor:=crDrag;
SbDesk.Hint:='����� ������';
SbDesk.ShowHint:= True;
end;

procedure TMainForm.sbCrTxtClick(Sender: TObject);
begin
sbCrTxt.Down:=True;
NeedCreate:=2;
sbDesk.Cursor:=crDrag;
SbDesk.Hint:='����� ���� �����';
SbDesk.ShowHint:= True;
end;

procedure TMainForm.sbCrLabClick(Sender: TObject);
begin
sbCrLab.Down:=True;
NeedCreate:=3;
sbDesk.Cursor:=crDrag;
SbDesk.Hint:='����� �������';
SbDesk.ShowHint:= True;
end;

procedure TMainForm.pmDelClick(Sender: TObject);
var i:integer;
begin
Panel:=PanelList.Items[CurrentPanel];
PanelList.Delete(CurrentPanel);
Panel.Free;
Count:=PanelList.Count-1;
CurrentPanel:=Count;
for i:=0 to Count do
     begin
     Panel:=PanelList.Items[i];
     Panel.Tag:=i;
     end;
SbDeskClick(Sender);
end;

procedure TMainForm.SgPropKeyPress(Sender: TObject; var Key: Char);
begin
if (SgProp.Col<4) then
     begin
     if Key=#8 then SgProp.Cells[SgProp.Col,1]:='' else if not(Key in['0'..'9'])then Key:=#0;
     end else if (PanelList.Count>0) then
     begin
     Panel:=PanelList.Items[CurrentPanel];
     Panel.Caption:=SgProp.Cells[4,1];
     end;
end;

procedure TMainForm.SgPropKeyDown(Sender: TObject; var Key: Word; Shift: TShiftState);
var i,T1,L1:integer;
begin
if (Key=VK_RETURN)and(PanelList.Count>0) then
     begin
     Panel:=PanelList.Items[CurrentPanel];
     with Panel do
          begin
          T1:=Top;
          L1:=Left;
          L0:=Left;
          T0:=Top;
          H0:=Height;
          W0:=Width;;
          Lk:=Left;
          Tk:=Top;
          Hk:=Height;
          Wk:=Width;
          end;
     i:=SgProp.Col;
          case i of
          0:   begin //left
               with sbDesk do
                    begin
                         try Lk:=StrToInt(SgProp.Cells[0,1])-HorzScrollBar.Position;
                         except on E: EConvertError do end;
                    if Lk<-HorzScrollBar.Position then Lk:=-HorzScrollBar.Position+1;
                    if Lk+Wk+HorzScrollBar.Position>HorzScrollBar.Range then
                         Lk:=HorzScrollBar.Range-Wk-HorzScrollBar.Position-1;
                    end;
                    Count:=PanelList.Count-1;
               for i:=0 to Count do
                    begin
                    if i<>CurrentPanel then
                         begin
                         Panel:=PanelList.Items[i];
                         with Panel do
                              begin
                              if (L1>Left)and(T1+Hk>Top)and(T1<Top+Height)and(Lk<Left+Width)then Lk:=Left+Width;
                              if (L1<Left)and(T1+Hk>Top)and(T1<Top+Height)and(Lk+Wk>Left)then Lk:=Left-Wk;
                              end;
                         end;
                    end;
               end;
          1:   begin //top
               with sbDesk do
                    begin
                         try Tk:=StrToInt(SgProp.Cells[1,1])-VertScrollBar.Position;
                         except on E: EConvertError do end;
                    if Tk<-VertScrollBar.Position then Tk:=-VertScrollBar.Position+1;
                    if Tk+Hk+VertScrollBar.Position>VertScrollBar.Range then
                         Tk:=VertScrollBar.Range-Hk-VertScrollBar.Position-1;
                    end;
                    Count:=PanelList.Count-1;
               for i:=0 to Count do
                    begin
                    if i<>CurrentPanel then
                         begin
                         Panel:=PanelList.Items[i];
                         with Panel do
                              begin
                              if (T1>Top)and(L1<Left+Width)and(L1+Wk>Left)and(Tk<Top+Height) then Tk:=Top+Height;
                              if (T1<Top)and(L1<Left+Width)and(L1+Wk>Left)and(Tk+Hk>Top) then Tk:=Top-Hk;
                              end;
                         end;
                    end;
               end;
          2:   begin //width
                    try Wk:=StrToInt(SgProp.Cells[2,1]);
                    except on E: EConvertError do end;
               Count:=PanelList.Count-1;
               for i:=0 to Count do
                    begin
                    if i<>CurrentPanel then
                         begin
                         Panel:=PanelList.Items[i];
                         with Panel do if (Lk<Left)and(Tk+Hk>Top)and(Tk<Top+Height)and(Lk+Wk>Left) then Wk:=Left-Lk;
                         end;
                    end;
               if Lk+Wk+SbDesk.HorzScrollBar.Position > SbDesk.HorzScrollBar.Range then
                    Wk:=SbDesk.HorzScrollBar.Range-Lk-SbDesk.HorzScrollBar.Position;
               if Wk < MinWidth then Wk:=MinWidth;
               end;
          3:   begin //height
               if Panel.BevelOuter<>bvLowered then
                    begin
                         try Hk:=StrToInt(SgProp.Cells[3,1]);
                         except on E: EConvertError do end;
                    if Tk+Hk+SbDesk.VertScrollBar.Position > SbDesk.VertScrollBar.Range then
                         Hk:=SbDesk.VertScrollBar.Range-Tk-SbDesk.VertScrollBar.Position;
                    Count:=PanelList.Count-1;
                    for i:=0 to Count do
                         begin
                         if i<>CurrentPanel then
                              begin
                              Panel:=PanelList.Items[i];
                              with Panel do if (Tk<Top)and(Lk<Left+Width)and(Lk+Wk>Left)and(Tk+Hk>Top)then
                                   Hk:=Top-Tk;
                              end;
                         end;
                    if Hk < MinHeight then Hk:=MinHeight;
                    end;
               end;
          4:   begin
               Panel.Caption:=SgProp.Cells[4,1];
               end;
          end;
     Refresh(Sender);
     end;
end;

procedure TMainForm.SbDeskClick(Sender: TObject);
var i:integer;
begin
if NeedCreate=0 then
     begin
     for i:=0 to MainForm.ComponentCount-1 do if MainForm.Components[i] is TShape then
          TShape(MainForm.Components[i]).Visible:=False;
     for i:=0 to 4 do SgProp.Cells[i, 1]:='';
     mnDel.Enabled:=False;
     mnDel.ShortCut:=ShortCut(0, []);
     end;
end;

procedure TMainForm.FormClose(Sender: TObject; var Action: TCloseAction);
var DialogValue: Integer;
begin
if Modified then
     begin
     DialogValue:=MessageDlg('��������� ��������� � �����?', mtWarning, [mbYes, mbNo], 0);
     if DialogValue=mrYes then mnSaveClick(Sender);
     end;
if FileExists('editor_tmp.htm') then DeleteFile('editor_tmp.htm');     
end;

procedure TMainForm.SgPropClick(Sender: TObject);
begin
mnDel.Enabled:=False;
mnDel.ShortCut:=ShortCut(0, []);
end;

procedure TMainForm.sbSelectClick(Sender: TObject);
begin
sbDesk.Cursor:=crDefault;
sbSelect.Down:=True;
NeedCreate:=0;
SbDesk.ShowHint:=False;
end;

procedure TMainForm.SbDeskMouseDown(Sender: TObject; Button: TMouseButton; Shift: TShiftState; X, Y: Integer);
begin
if (NeedCreate<>0)and Valid then
     begin
     PanelList.Add(TPanel.Create(Self));
     Count:=PanelList.Count-1;
     Panel:=PanelList.Items[Count];
     with Panel do
          begin
          Parent:=SbDesk;
          Tag:=Count;
          Cursor:=crSizeAll;
          BevelWidth:=2;
          PopupMenu:=PopupMenu1;
          OnMouseDown:=PanelMouseDown;
          OnMouseUp:=PanelMouseDown;
          OnMouseMove:=PanelMouseMove;
          end;
     Lk:=X;
     Tk:=Y;
     Wk:=DefaultWidth;
     Hk:=DefaultHeight;
          case NeedCreate of
          1:   begin
               SgProp.Cells[4, 0]:='Caption';
               with Panel do
                    begin
                    BevelOuter:=bvRaised;
                    Color:=clBtnFace;
                    Alignment:=taCenter;
                    Caption:='Button'+IntToStr(Count);
                    end;
               end;
          2:   begin
               SgProp.Cells[4, 0]:='Text';
               with Panel do
                    begin
                    BevelOuter:=bvLowered;
                    Color:=clHighlightText;
                    Alignment:=taLeftJustify;
                    Caption:='TextEdit'+IntToStr(Count);
                    end;
               end;
          3:   begin
               SgProp.Cells[4, 0]:='Text';
               with Panel do
                    begin
                    BevelOuter:=bvNone;
                    Color:=clBtnFace;
                    Alignment:=taLeftJustify;
                    Caption:='Label'+IntToStr(Count);
                    end;
               end;
          end;
     sbSelectClick(Sender);
     CurrentPanel:=Count;
     Refresh(Sender);
     end;
end;

procedure TMainForm.SbDeskMouseMove(Sender: TObject; Shift: TShiftState; X, Y: Integer);
var
  i:integer;
begin
if NeedCreate<>0 then
     begin
          i:=0;
          Valid:=True;
          repeat
          if MainForm.Components[i] is TPanel then with TPanel(MainForm.Components[i]) do
          if (Y+DefaultHeight>Top)and(Y<Top+Height)and(X+DefaultWidth>Left)and(X<Left+Width)then Valid:=False;
          i:=i+1;
          until (Valid=False)or(i=MainForm.ComponentCount);
     if Valid then
          begin
          sbDesk.Cursor:=crDrag;
          SbDesk.ShowHint:=True;
          end else
          begin
          sbDesk.Cursor:=crNoDrop;
          SbDesk.ShowHint:=False;
          end;
     end;
end;

procedure TMainForm.mnViewWebClick(Sender: TObject);
var
TempString : array[0..79] of char;
i,j:integer;
begin
j:=1;
SetLength(Prop_i, 7, 1);
SetLength(Prop_s, 1);
for i:=0 to MainForm.ComponentCount-1 do if MainForm.Components[i] is TPanel then
     with TPanel(MainForm.Components[i]) do
     begin
     SetLength(Prop_i, 7, j+1);
     SetLength(Prop_s, j+1);
     if BevelOuter=bvRaised then Prop_i[0, j]:=1;
     if BevelOuter=bvLowered then Prop_i[0, j]:=2;
     if BevelOuter=bvNone then Prop_i[0, j]:=3;
     Prop_i[1, j]:=Left+sbDesk.HorzScrollBar.Position;
     Prop_i[2, j]:=Top+sbDesk.VertScrollBar.Position;
     Prop_i[3, j]:=Width;
     Prop_i[4, j]:=Height;
     Prop_s[j]:=Caption;
     j:=j+1;
     end;
if j>1 then
     begin
     WriteHTMLFile('editor_tmp.htm', Prop_i, Prop_s);
     StrPCopy(TempString, 'editor_tmp.htm');
     ShellExecute(0, Nil, TempString, Nil, Nil, SW_NORMAL);
     end;
end;

end.