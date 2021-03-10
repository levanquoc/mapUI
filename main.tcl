#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Feb 18, 2021 02:22:44 AM GMT  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1920x927+57+70
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 136 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    labelframe $top.lab55 \
        -font TkDefaultFont -foreground black -relief raised \
        -background $vTcl(actual_gui_bg) -height 241 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 380 
    vTcl:DefineAlias "$top.lab55" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab55
    button $site_3_0.but56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command createRFID \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text RFID 
    vTcl:DefineAlias "$site_3_0.but56" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command createLinehorizontal \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text LINE 
    vTcl:DefineAlias "$site_3_0.but57" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command createLinevertical \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text LINE 
    vTcl:DefineAlias "$site_3_0.but58" "Button3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab60 \
        -activebackground #f9f9f9 -activeforeground black -background #000000 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_3_0.lab60" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab61 \
        -activebackground #f9f9f9 -activeforeground black -background #000000 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$site_3_0.lab61" "Label3" vTcl:WidgetProc "Toplevel1" 1
    labelframe $site_3_0.lab48 \
        -font TkDefaultFont -foreground black -background #0000a0 -height 55 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 52 
    vTcl:DefineAlias "$site_3_0.lab48" "Labelframe2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command crossroadLine \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text CROSSROAD 
    vTcl:DefineAlias "$site_3_0.but45" "Button13" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but56 \
        -in $site_3_0 -x 0 -relx 0.105 -y 0 -rely 0.043 -width 77 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but57 \
        -in $site_3_0 -x 0 -relx 0.105 -y 0 -rely 0.26 -width 77 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but58 \
        -in $site_3_0 -x 0 -relx 0.105 -y 0 -rely 0.476 -width 77 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab60 \
        -in $site_3_0 -x 0 -relx 0.42 -y 0 -rely 0.346 -width 0 \
        -relwidth 0.113 -height 0 -relheight 0.03 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab61 \
        -in $site_3_0 -x 0 -relx 0.472 -y 0 -rely 0.476 -width 0 \
        -relwidth 0.026 -height 0 -relheight 0.186 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.42 -y 0 -rely 0.043 -width 0 \
        -relwidth 0.136 -height 0 -relheight 0.238 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 0 -relx 0.105 -y 0 -rely 0.736 -width 77 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    canvas $top.can45 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -closeenough 1.0 \
        -height 581 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -insertbackground black -relief ridge \
        -selectbackground blue -selectforeground white -width 842 
    vTcl:DefineAlias "$top.can45" "mapFrame" vTcl:WidgetProc "Toplevel1" 1
    labelframe $top.lab47 \
        -font TkDefaultFont -foreground black -text PROPERTY_LINE \
        -background $vTcl(actual_gui_bg) -height 339 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 378 
    vTcl:DefineAlias "$top.lab47" "Labelframe3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab47
    entry $site_3_0.ent52 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 74 
    vTcl:DefineAlias "$site_3_0.ent52" "lenlineEntry" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Head 
    vTcl:DefineAlias "$site_3_0.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo46 \
        -values None','Line','Hook','Position -exportselection 0 \
        -font TkTextFont -state readonly -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo46" "functionEntry" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Rotate type} 
    vTcl:DefineAlias "$site_3_0.lab47" "Label4" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo48 \
        -values Front','Back -font TkTextFont -state readonly -foreground {} \
        -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo48" "headEntry" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Len 
    vTcl:DefineAlias "$site_3_0.lab46" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Degree rote} 
    vTcl:DefineAlias "$site_3_0.lab48" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Command 
    vTcl:DefineAlias "$site_3_0.lab49" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Line type} 
    vTcl:DefineAlias "$site_3_0.lab50" "Label9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Speed max} 
    vTcl:DefineAlias "$site_3_0.lab51" "Label10" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Wait time} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label11" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Fucntion 
    vTcl:DefineAlias "$site_3_0.lab53" "Label12" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab54 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Index 
    vTcl:DefineAlias "$site_3_0.lab54" "Label13" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo56 \
        -values None','Center','Side -font TkTextFont -state readonly \
        -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo56" "rotatetypeEntry" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo58 \
        -values {"None','Center','Left','Right"} -font TkTextFont \
        -state readonly -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo58" "commandEntry" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo59 \
        -values {"One','Fork Left','Fork Right','Cross"} -font TkTextFont \
        -state readonly -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo59" "linetypeEntry" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo60 \
        -values {"Slow','Normal','High"} -font TkTextFont -state readonly \
        -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo60" "speedmaxEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent63 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 74 
    vTcl:DefineAlias "$site_3_0.ent63" "waittimeEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent64 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 74 
    vTcl:DefineAlias "$site_3_0.ent64" "indexLineEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent45 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 64 
    vTcl:DefineAlias "$site_3_0.ent45" "degreeroteEntry" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent52 \
        -in $site_3_0 -x 0 -relx 0.235 -y 0 -rely 0.285 -width 74 -relwidth 0 \
        -height 27 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 0 -relx 0.026 -y 0 -rely 0.588 -width 0 \
        -relwidth 0.143 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo46 \
        -in $site_3_0 -x 0 -relx 0.235 -y 0 -rely 0.408 -width 0 \
        -relwidth 0.193 -height 0 -relheight 0.097 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.026 -y 0 -rely 0.706 -width 0 \
        -relwidth 0.169 -height 0 -relheight 0.091 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo48 \
        -in $site_3_0 -x 0 -relx 0.238 -y 0 -rely 0.559 -width 0 \
        -relwidth 0.193 -height 0 -relheight 0.097 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.026 -y 0 -rely 0.288 -width 0 \
        -relwidth 0.116 -height 0 -relheight 0.078 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.529 -y 0 -rely 0.122 -width 0 \
        -relwidth 0.169 -height 0 -relheight 0.066 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.529 -y 0 -rely 0.279 -width 0 \
        -relwidth 0.169 -height 0 -relheight 0.066 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.529 -y 0 -rely 0.414 -width 0 \
        -relwidth 0.143 -height 0 -relheight 0.066 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.529 -y 0 -rely 0.588 -width 0 \
        -relwidth 0.169 -height 0 -relheight 0.065 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.529 -y 0 -rely 0.735 -width 0 \
        -relwidth 0.143 -height 0 -relheight 0.035 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 0 -relx 0.026 -y 0 -rely 0.412 -width 0 \
        -relwidth 0.169 -height 0 -relheight 0.065 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 0 -relx 0.053 -y 0 -rely 0.135 -width 0 \
        -relwidth 0.077 -height 0 -relheight 0.063 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo56 \
        -in $site_3_0 -x 0 -relx 0.238 -y 0 -rely 0.706 -width 0 \
        -relwidth 0.193 -height 0 -relheight 0.097 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo58 \
        -in $site_3_0 -x 0 -relx 0.751 -y 0 -rely 0.25 -width 0 \
        -relwidth 0.193 -height 0 -relheight 0.097 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo59 \
        -in $site_3_0 -x 0 -relx 0.741 -y 0 -rely 0.402 -width 0 \
        -relwidth 0.193 -height 0 -relheight 0.096 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo60 \
        -in $site_3_0 -x 0 -relx 0.741 -y 0 -rely 0.585 -width 0 \
        -relwidth 0.193 -height 0 -relheight 0.096 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent63 \
        -in $site_3_0 -x 0 -relx 0.741 -y 0 -rely 0.71 -width 74 -relwidth 0 \
        -height 27 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent64 \
        -in $site_3_0 -x 0 -relx 0.233 -y 0 -rely 0.125 -width 74 -relwidth 0 \
        -height 27 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent45 \
        -in $site_3_0 -x 0 -relx 0.751 -y 0 -rely 0.124 -width 64 -relwidth 0 \
        -height 27 -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab45 \
        -font TkDefaultFont -foreground black -text RFID \
        -background $vTcl(actual_gui_bg) -height 96 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 380 
    vTcl:DefineAlias "$top.lab45" "Labelframe5" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab45
    label $site_3_0.lab46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Name 
    vTcl:DefineAlias "$site_3_0.lab46" "Label6" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent47 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 64 
    vTcl:DefineAlias "$site_3_0.ent47" "nameRFIDEntry" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Index 
    vTcl:DefineAlias "$site_3_0.lab45" "Label14" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent46 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 64 
    vTcl:DefineAlias "$site_3_0.ent46" "indexCardEntry" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.026 -y 0 -rely 0.549 -width 0 \
        -relwidth 0.224 -height 0 -relheight 0.11 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent47 \
        -in $site_3_0 -x 0 -relx 0.316 -y 0 -rely 0.515 -width 64 -relwidth 0 \
        -height 27 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 0 -relx 0.039 -y 0 -rely 0.22 -width 0 \
        -relwidth 0.195 -height 0 -relheight 0.209 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent46 \
        -in $site_3_0 -x 0 -relx 0.316 -y 0 -rely 0.134 -width 64 -relwidth 0 \
        -height 27 -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab48 \
        -font TkDefaultFont -foreground black -text Labelframe \
        -background $vTcl(actual_gui_bg) -height 145 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 378 
    vTcl:DefineAlias "$top.lab48" "Labelframe6" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab48
    label $site_3_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Start 
    vTcl:DefineAlias "$site_3_0.lab49" "Label15" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text End 
    vTcl:DefineAlias "$site_3_0.lab50" "Label16" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent51 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 64 
    vTcl:DefineAlias "$site_3_0.ent51" "startEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent52 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 64 
    vTcl:DefineAlias "$site_3_0.ent52" "endEntry" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command send \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text SEND 
    vTcl:DefineAlias "$site_3_0.but53" "Button5" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo45 \
        -values {"1','2','3','4','5','6','7','8','9','10"} -font TkTextFont \
        -textvariable combobox -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo45" "routeEntry" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Route 
    vTcl:DefineAlias "$site_3_0.lab46" "Label17" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command setupStep \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text OK 
    vTcl:DefineAlias "$site_3_0.but45" "Button7" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command reset \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text RESET 
    vTcl:DefineAlias "$site_3_0.but46" "Button8" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.053 -y 0 -rely 0.4 -width 0 \
        -relwidth 0.143 -height 0 -relheight 0.145 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.053 -y 0 -rely 0.552 -width 0 \
        -relwidth 0.143 -height 0 -relheight 0.145 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent51 \
        -in $site_3_0 -x 0 -relx 0.212 -y 0 -rely 0.414 -width 63 -relwidth 0 \
        -height 17 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent52 \
        -in $site_3_0 -x 0 -relx 0.209 -y 0 -rely 0.552 -width 64 -relwidth 0 \
        -height 17 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but53 \
        -in $site_3_0 -x 0 -relx 0.45 -y 0 -rely 0.759 -width 67 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tCo45 \
        -in $site_3_0 -x 0 -relx 0.217 -y 0 -rely 0.207 -width 0 \
        -relwidth 0.14 -height 0 -relheight 0.145 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.085 -y 0 -rely 0.214 -width 0 \
        -relwidth 0.116 -height 0 -relheight 0.145 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 0 -relx 0.132 -y 0 -rely 0.759 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 0 -relx 0.291 -y 0 -rely 0.759 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab55 \
        -in $top -x 0 -relx 0.005 -y 0 -rely 0.019 -width 0 -relwidth 0.198 \
        -height 0 -relheight 0.229 -anchor nw -bordermode ignore 
    place $top.can45 \
        -in $top -x 0 -relx 0.224 -y 0 -rely 0.012 -width 0 -relwidth 0.788 \
        -height 0 -relheight 0.972 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.005 -y 0 -rely 0.259 -width 0 -relwidth 0.197 \
        -height 0 -relheight 0.348 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 0 -relx 0.005 -y 0 -rely 0.615 -width 0 -relwidth 0.198 \
        -height 0 -relheight 0.098 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.005 -y 0 -rely 0.723 -width 0 -relwidth 0.197 \
        -height 0 -relheight 0.156 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
