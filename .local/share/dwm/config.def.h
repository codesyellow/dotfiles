/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 1;        /* border pixel of windows */
static const unsigned int snap      = 32;       /* snap pixel */
static const int showbar            = 1;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
static const int bordersize = 1;
/*  Display modes of the tab bar: never shown, always shown, shown only in  */
/*  monocle mode in the presence of several windows.                        */
/*  Modes after showtab_nmodes are disabled.                                */
enum showtab_modes { showtab_never, showtab_auto, showtab_nmodes, showtab_always};
static const int showtab			= showtab_auto;        /* Default tab bar show mode */
static const int toptab				= False;               /* False means bottom tab bar */
static const int attachbelow = 1;    /* 1 means attach after the currently active window */

static const char *fonts[]          = { 
  "JetBrainMono Nerd Font",
  "Symbols Nerd Font:size=11",
};
static const char dmenufont[] = "JetBrainMono Nerd Font:size=12";
static const char prompt_icon[] = "";
static const char bg1[]       = "#4c566a";
static const char bg0[]       = "#2e3440";
static const char fg0[]       = "#eceff4";
static const char light[]     = "#f9e2af";
static const char fg1[]       = "#eceff4";
static const char border[]    = "#36C2CE";
static const char *colors[][3]= {
  /*               fg         bg         border   */
  [SchemeNorm] = { fg0, bg0, bg0 },
  [SchemeSel]  = { light, bg0,  light  },
};

/* tagging */
static char *tags[] = { " ", "", "", "" };
static const int taglayouts[] = { 2, 2, 2, 2, 2, };

static const Rule rules[] = {
  /* xprop(1):
   *	WM_CLASS(STRING) = instance, class
   *	WM_NAME(STRING) = title
   */
  /* class      instance    title       tags mask     isfloating   monitor    float x,y,w,h         floatborderpx*/
  { "Gimp",     NULL,       NULL,       0,            1,           -1,   0,     50,50,500,500,        5 },
  { "firefox",  NULL,       NULL,       1 << 0,       0,           -1,   0,     50,50,500,500,        5 },
  { "kitty",  NULL,       NULL,       2 << 0,       0,           -1,   0,     50,50,500,500,        5 },
  { "Brave-browser",  NULL,       NULL,       1 << 0,       0,           -1,   0,     50,50,500,500,        5 },
  { NULL,  "Navigator",       NULL,       1 << 0,       0,           -1,   0,     50,50,500,500,        5 },
  { "Emacs",    NULL,       NULL,       1 << 0,       0,           -1,   0,     50,50,500,500,        5 },
  { "mpv",  NULL,       NULL,       1 << 2,       0,           -1,   0,     50,50,500,500,        5 },
  { "TelegramDesktop",  NULL,       NULL,       1 << 2,       0,           -1,   0,     50,50,500,500,        5 },
  { "st-256color",  NULL,       NULL,       1 << 1,       0,           -1,   0,     50,50,500,500,        5 },
  { "Whatsapp-for-linux",  NULL,       NULL,       0,       1,           -1,   0,     50,50,1100,600,        5 },
  { "WhatSie",  NULL,       NULL,       0,       1,           -1,   0,     50,50,1100,600,        5 },
  { "Zathura",  NULL,       NULL,       1 << 2,       0,           -1,        50,50,500,500,        5,      0},
  { "steam",    "steamwebhelper",       NULL,       1 << 3,       0,           -1, 0,        50,50,500,500,        5},
  { "Input-remapper-gtk",    NULL,       NULL,       1 << 3,       0,           -1, 0,        50,50,500,500,        5},
  { NULL,    NULL,       "doc-240913062405 (/tmp/vim-anywhere) - GVIM",       0,       1,           -1, 0,        80,50,1200,400,        bordersize},
  { "sober",    NULL,       NULL,       1 << 3,       0,           -1, 0,        50,50,500,500,        5},
  { "alacritty",    NULL,       NULL,       1 << 2,       0,           -1, 0,        50,50,500,500,        5},
  { "ProtonUp-Qt",    NULL,       NULL,       1 << 3,       0,           -1, 0,        50,50,500,500,        5},
  { NULL,    NULL,       "Steam",       1 << 3,       0,           -1,     0,   50,50,500,500,        5},
  { NULL,    NULL,       "Steam setup",       1 << 3,       0,           -1,        50,50,500,500,        50},
  { "heroic",   NULL,       NULL,       1 << 3,       0,           -1,    0,    50,50,500,500,        5},
  { "cage",   NULL,       NULL,       1 << 3,       0,           -1,    0,    50,50,500,500,        5},
  { "retroarch",   NULL,       NULL,       1 << 3,       0,           -1,    0,    50,50,500,500,        5},
  { "Lutris",   NULL,       NULL,       1 << 3,       0,           -1,    0,    50,50,500,500,        5},
  { NULL,  "youtube music",       NULL,       1 << 4,       0,           -1, 0,    50,50,500,500,        5},
  // floating
  { "h-m-m",   NULL,       NULL,       0,       1,           -1,    0,    180,134,1000,500,        bordersize},
  // scratchpads
  { NULL,       NULL,   "scratchpad",   0,            1,           -1,   's', 80,448,1200,300,        bordersize,   },
  { NULL,       NULL,   "habits",   0,            1,           -1,   'h', 80,50,1200,400,        bordersize,   },
  { NULL,       NULL,   "task-tui",   0,            1,           -1,   't', 840,59,500,650,        bordersize,   },
  { NULL,       NULL,   "ai",   0,            1,           -1,   'a', 840,59,500,650,        bordersize,   },
  { NULL,       NULL,   "pulsemixer",   0,            1,           -1,   'p', 778,48,400,400,        bordersize,   },
  { NULL,       NULL,   "btop",   0,            1,           -1,   'b', 80,84,1200,600,        bordersize,   },
  { NULL,       NULL,   "cmus",   0,            1,           -1,   'u', 80,84,1200,600,        bordersize,   },
  { NULL,       NULL,   "bluetui",   0,            1,           -1,   'f', 80,80,1200,600,        bordersize,   },
  {"calc",       NULL,   NULL,   0,            1,           -1,   'g', 530,234,300,300,        bordersize,   },
  { NULL,       NULL,   "WhatsApp for Linux",   0,            1,           -1,   'w', 80,80,1200,600,        bordersize,   },
 // { NULL,       NULL,   "WhatSie",   0,            1,           -1,   'w', 80,80,1200,600,        bordersize,   },
  { NULL,       NULL,   "Free Download Manager",   0,            1,           -1,   'd', 80,80,1200,600,        bordersize,   },
  { NULL,       NULL,   "notes",   0,            1,           -1,   'o', 80,50,1200,600,        bordersize,   },
  { NULL,       NULL,   "tt",   0,            1,           -1,   'e', 80,50,1200,600,        bordersize,   },
  { NULL,       NULL,   "Exercise Timer",   0,            1,           -1,   'z', 500,50,400,400,        bordersize,   },
  { NULL,       NULL,   "clock",   0,            1,           -1,   'c', 555,184,450,280,        bordersize,   },
  { "trayer",       NULL,   "panel",   0,            1,           -1,   'q', 500,50,400,400,        bordersize,   },
};

/* layout(s) */
static const float mfact     = 0.70; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 0;    /* 1 means respect size hints in tiled resizals */
static const int lockfullscreen = 1; /* 1 will force focus on the fullscreen window */

static const Layout layouts[] = {
  /* symbol     arrange function */
  { "[]=",      tile },    /* first entry is default */
  { "",        NULL },    /* no layout function means floating behavior */
  { "",        monocle },
  { "",        bstack },
  { "===",      bstackhoriz },
};

/* custom symbols for nr. of clients in monocle layout */
/* when clients >= LENGTH(monocles), uses the last element */
static const char *monocles[] = { "" };
/* key definitions */
#define CONCAT_XK(KEY) XK_##KEY
#define MODKEY Mod4Mask
#define TAGKEYS(KEY,TAG)                                                                                              \
  &((Keychord){2, {{MODKEY, XK_w}, {0, CONCAT_XK(KEY)}},                           view,           {.ui = 1 << TAG} }),\
  &((Keychord){2, {{MODKEY|ShiftMask, XK_w}, {0, CONCAT_XK(KEY)}},                           tag,            {.ui = 1 << TAG} }), 
/*       &((Keychord){1, {{MODKEY|ControlMask, KEY}},                            toggleview,     {.ui = 1 << TAG} }), \
         &((Keychord){1, {{MODKEY|ControlMask|ShiftMask, KEY}},                  toggletag,      {.ui = 1 << TAG} }),*/

#define SCRATCHS(KEY,SCRATCH)                                                                                        \
  &((Keychord){2, {{MODKEY, XK_s}, {0, CONCAT_XK(KEY)}},                           togglescratch,  {.v = SCRATCH } }), 

#define EXECS(KEY,EXEC)                                                                                              \
  &((Keychord){2, {{MODKEY, XK_e}, {0, CONCAT_XK(KEY)}}, spawn, {.v = EXEC }}),

#define STACKKEYS(MOD,ACTION)                                                                                              \
  &((Keychord){1, {{MOD, XK_j}},  ACTION##stack, {.i = INC(+1)}}), \
  &((Keychord){1, {{MOD, XK_k}}, ACTION##stack, {.i = INC(-1)}}), \
  &((Keychord){1, {{MOD, XK_b}}, ACTION##stack, {.i = PREVSEL}}), \
  &((Keychord){1, {{MOD, XK_m}},  ACTION##stack, {.i = 0}}), \
  &((Keychord){1, {{MOD, XK_r}},  ACTION##stack, {.i = 1}}), \
  &((Keychord){1, {{MOD, XK_z}},  ACTION##stack, {.i = 2}}), \
  &((Keychord){1, {{MOD, XK_x}},  ACTION##stack, {.i = -1}}), \
/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

/* commands */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
static const char *dmenucmd[] = { "dmenu_run", "-nb", bg0, "-z", "497", "-x", "200", "-y", "1", "-sb", bg0, "-shb", bg0, "-nhb", bg0, "-shf", light,"-nhf",border,"-fn", dmenufont, "-p", prompt_icon, NULL };
static const char *dmenumpv[] = { "mpvtube.sh", NULL };
static const char *clipmenucmd[] = { "clipmenu", "-z", "700", "-x", "230", "-y", "4", "-nb", bg0, NULL };
static const char *bass[] = { "easy_preset.sh", "HeavyBass", NULL};
static const char *loudness[] = { "easy_preset.sh", "LoudnessEqualizer", NULL};
static const char *termcmd[]  = { "st", "-T", "tmux", "-e", "tmux", NULL };
static const char *game_to_list[]  = { "game_to_list.sh", NULL };
static const char *pymors[]  = { "pymor", "-t", "20", NULL };
static const char *pymorl[]  = { "pymor", "-t", "20", "-f", "3", NULL };
static const char *pymorc[]  = { "pymor", "-c", NULL };
static const char *stretch[]  = { "stretch.sh", "-t", "15", "-s", "12", "-w", "3", NULL };
static const char *dunst[]  = { "dunstctl", "close-all", NULL };
static const char *rotatemouse[]  = { "360.sh", "99", NULL };
static const char *borderless[]  = { "borderless.sh",  NULL };
static const char *browser[]  = { "flatpak", "run", "io.github.zen_browser.zen",  NULL };
static const char *mindmap[] = {  "maps.sh", NULL };
static const char *vimanywhere[] = {  "/home/cie/.vim-anywhere/bin/run", NULL };
/*First arg only serves to match against key in rules*/
static const char *scratchpadcmd[] = {"s", "alacritty", "--config-file", "/home/digo/.config/alacritty/scratchpad.toml", "--class", "scratchpad", "-t", "scratchpad", "-e", "bash", "-c", "tmux attach-session -t scratch || tmux new-session -s scratch", NULL}; 
static const char *scratchpadclock[] = {"c", "st", "-t", "clock", "-c","clock", "-e", "tclock_timer.sh", NULL}; 
static const char *scratchpadcalc[] = {"g", "st", "-t", "calc", "-c","calc", "-e", "bc", NULL}; 
static const char *scratchpadnotes[] = {"o", "st", "-t", "notes", "-c","notes", "-e", "vim", "/home/digo/.vimwiki/notes/index.wiki", NULL}; 
static const char *scratchpadbtop[] = {"b", "st", "-t", "btop", "-c","btop", "-e", "btop", NULL}; 
static const char *scratchpadtask[] = {"t", "st", "-t", "task-tui", "-c","task-tui", "-e", "taskwarrior-tui", NULL}; 
static const char *scratchpadmixer[] = {"p", "st", "-t", "pulsemixer", "-c","pulsemixer", "-e", "pulsemixer", NULL}; 
static const char *scratchpadtt[] = {"e", "st", "-t", "tt", "-c","tt", "-e", "tt", NULL}; 
static const char *scratchpadai[] = {"a", "st", "-t", "ai", "-c","aichat", "-e", "aichat", NULL}; 
static const char *scratchpadcmus[] = {"u", "st", "-t", "cmus", "-c","cmus", "-e", "cmus", NULL}; 
static const char *scratchpadhabit[] = {"h", "st", "-t", "habits", "-c","habits", "-e", "vim", "/home/digo/.vimwiki/habits/index.wiki", NULL}; 
static const char *scratchfdm[] = {"d", "fdm", NULL}; 
static const char *scratchpadzap[] = {"w", "whatsapp-for-linux", NULL}; 
static const char *scratchpadtrayer[] = {"q", "trayer", "--widthtype", "pixel", "--transparent", "true", "--alpha", "255", "--distance", "10", NULL}; 

static Keychord *keychords[] = {
  /* Keys        function        argument */
  // clients
  &((Keychord){2, {{MODKEY, XK_c}, {0, XK_f}},                            togglefullscr,  {0}}),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_f}},                             togglefullscr,  {0}}),
  &((Keychord){2, {{MODKEY, XK_c}, {0, XK_o}},                            togglefloating, {0} }),
  // layouts
  &((Keychord){2, {{MODKEY, XK_l}, {0, XK_1}},                            setlayout,      {.v = &layouts[0]}}),
  &((Keychord){2, {{MODKEY, XK_l}, {0, XK_2}},                            setlayout,      {.v = &layouts[1]}}),
  &((Keychord){2, {{MODKEY, XK_l}, {0, XK_t}},                            setlayout,      {.v = &layouts[2]}}),
  &((Keychord){2, {{MODKEY, XK_l}, {0, XK_b}},                            setlayout,      {.v = &layouts[3]}}),
  &((Keychord){2, {{MODKEY, XK_l}, {0, XK_5}},                            setlayout,      {.v = &layouts[4]}}),
  // scratchs
  SCRATCHS(p, scratchpadmixer)
  SCRATCHS(u, scratchpadcmd)
  SCRATCHS(t, scratchpadtask)
  SCRATCHS(r, scratchpadclock)
  SCRATCHS(s, scratchpadtrayer)
  SCRATCHS(i, scratchpadai)
  SCRATCHS(k, scratchpadtt)
  SCRATCHS(h, scratchpadhabit)
  SCRATCHS(n, scratchpadnotes)
  SCRATCHS(d, scratchfdm)
  SCRATCHS(w, scratchpadzap)
  SCRATCHS(m, scratchpadbtop)
  SCRATCHS(g, scratchpadcalc)
  SCRATCHS(c, scratchpadcmus)
//  SCRATCHS(b, scratchpadblue)
  // exec
  EXECS(r, dmenucmd)
  EXECS(b, browser)
  EXECS(h, clipmenucmd)
  EXECS(s, rotatemouse)
  EXECS(v, dmenumpv)
  EXECS(e, vimanywhere)
  EXECS(n, dunst)
  EXECS(m, mindmap)
  EXECS(w, game_to_list)
  EXECS(t, stretch)
  STACKKEYS(MODKEY,                          focus)
	STACKKEYS(MODKEY|ShiftMask,                push)

  // volume
  &((Keychord){2, {{MODKEY, XK_v}, {0, XK_j}},                            spawn,         SHCMD("/home/digo/.bin/volume.sh down && /usr/bin/kill -30 $(cat ~/.cache/pidofbar)") }),
  &((Keychord){2, {{MODKEY, XK_v}, {0, XK_k}},                            spawn,         SHCMD("/home/digo/.bin/volume.sh up && /usr/bin/kill -30 $(cat ~/.cache/pidofbar)") }),
  &((Keychord){2, {{MODKEY, XK_v}, {0, XK_m}},                            spawn,         SHCMD("/home/digo/.bin/volume.sh mute && /usr/bin/kill -30 $(cat ~/.cache/pidofbar)") }),
  // action
  &((Keychord){2, {{MODKEY, XK_a}, {0, XK_m}},                 spawn,          {.v = bass } }),
  &((Keychord){2, {{MODKEY, XK_a}, {0, XK_l}},                 spawn,          {.v = loudness } }),
  &((Keychord){2, {{MODKEY, XK_a}, {0, XK_q}},                             quit,           {0} }),
  &((Keychord){2, {{MODKEY, XK_a}, {0, XK_k}},                             killclient,     {0} }),
  &((Keychord){2, {{MODKEY, XK_a}, {0, XK_b}},                             spawn,     {.v = borderless } }),
  // pymor
  &((Keychord){2, {{MODKEY, XK_p}, {0, XK_s}},                 spawn,          {.v = pymors } }),
  &((Keychord){2, {{MODKEY, XK_p}, {0, XK_l}},                 spawn,          {.v = pymorl } }),
  &((Keychord){2, {{MODKEY, XK_p}, {0, XK_c}},                 spawn,          {.v = pymorc } }),
  //rest
  //  &((Keychord){1, {{MODKEY, XK_p}},                                       spawn,          {.v = dmenucmd } }),
  &((Keychord){1, {{MODKEY, XK_t}},                                       spawn,          {.v = termcmd } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_b}},                                       togglebar,      {1} }),
//  &((Keychord){1, {{MODKEY, XK_j}},                                       focusstack,     {.i = +1 } }),
 // &((Keychord){1, {{MODKEY, XK_k}},                                       focusstack,     {.i = -1 } }),
  //  &((Keychord){1, {{MODKEY, XK_i}},                                       incnmaster,     {.i = +1 } }),
  //  &((Keychord){1, {{MODKEY, XK_d}},                                       incnmaster,     {.i = -1 } }),
  &((Keychord){1, {{MODKEY, XK_i}},                                       setmfact,       {.f = +0.05} }),
  &((Keychord){1, {{MODKEY, XK_d}},                                       setmfact,       {.f = -0.05} }),
  &((Keychord){1, {{MODKEY, XK_Return}},                                  zoom,           {0} }),
  &((Keychord){1, {{MODKEY, XK_Tab}},                                     view,           {0} }),
  //  &((Keychord){1, {{MODKEY, XK_space}},                                   setlayout,      {0} }),
  &((Keychord){1, {{MODKEY, XK_0}},                                       view,           {.ui = ~0 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_0}},                             tag,            {.ui = ~0 } }),
  &((Keychord){1, {{MODKEY, XK_comma}},                                   focusmon,       {.i = -1 } }),
  &((Keychord){1, {{MODKEY, XK_period}},                                  focusmon,       {.i = +1 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_comma}},                         tagmon,         {.i = -1 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_period}},                        tagmon,         {.i = +1 } }),
  TAGKEYS(                        b,                      0)
  TAGKEYS(                        t,                      1)
  TAGKEYS(                        v,                      2)
  TAGKEYS(                        r,                      3)
};


/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static const Button buttons[] = {
  /* click                event mask      button          function        argument */
///  { ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
  { ClkLtSymbol,          0,              Button3,        setlayout,      {.v = &layouts[2]} },
  { ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
  { ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
  { ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
  { ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
  { ClkTagBar,            0,              Button1,        view,           {0} },
  { ClkTagBar,            0,              Button3,        toggleview,     {0} },
  { ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
  { ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
  { ClkTabBar,            0,              Button1,        focuswin,       {0} },
};

