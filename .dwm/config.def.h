/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 1;        /* border pixel of windows */
static const unsigned int snap      = 32;       /* snap pixel */
static const int showbar            = 1;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
/*  Display modes of the tab bar: never shown, always shown, shown only in  */
/*  monocle mode in the presence of several windows.                        */
/*  Modes after showtab_nmodes are disabled.                                */
enum showtab_modes { showtab_never, showtab_auto, showtab_nmodes, showtab_always};
static const int showtab			= showtab_auto;        /* Default tab bar show mode */
static const int toptab				= False;               /* False means bottom tab bar */
static const char *fonts[]          = { 
  "Font Awesome 6 Free Solid:size=11",
   };
static const char dmenufont[]       = "monospace:size=10";
static const char bg1[]       = "#000000";
static const char col_gray2[]       = "#000000";
static const char col_gray3[]       = "#E4C59E";
static const char col_gray4[]       = "#ffffff";
static const char col_cyan[]        = "#543A48";
static const char *colors[][3]      = {
	/*               fg         bg         border   */
	[SchemeNorm] = { col_gray3, bg1, col_gray2 },
	[SchemeSel]  = { col_gray4, col_cyan,  col_cyan  },
};

/* tagging */
static const char *tags[] = { "I", "II", "IV", "V", "VI" };
static const int taglayouts[] = { 3, 3, 2, 2, 2, };

static const Rule rules[] = {
	/* xprop(1):
	 *	WM_CLASS(STRING) = instance, class
	 *	WM_NAME(STRING) = title
	 */
	/* class      instance    title       tags mask     isfloating   monitor    float x,y,w,h         floatborderpx*/
	{ "Gimp",     NULL,       NULL,       0,            1,           -1,   0,     50,50,500,500,        5 },
	{ "firefox",  NULL,       NULL,       1 << 0,       0,           -1,   0,     50,50,500,500,        5 },
	{ "st-256color",  NULL,       NULL,       1 << 1,       0,           -1,   0,     50,50,500,500,        5 },
  { "Alacritty",       "Alacritty",       NULL,       1 << 1,       0,           -1,0,        50,50,500,500,        5 },
  { "Zathura",  NULL,       NULL,       1 << 2,       0,           -1,        50,50,500,500,        5,      0},
  { "steam",    "steamwebhelper",       NULL,       1 << 3,       0,           -1, 0,        50,50,500,500,        5},
  { NULL,    NULL,       "Steam",       1 << 3,       0,           -1,     0,   50,50,500,500,        5},
  { NULL,    NULL,       "Steam setup",       1 << 3,       0,           -1,        50,50,500,500,        50},
  { "heroic",   NULL,       NULL,       1 << 3,       0,           -1,    0,    50,50,500,500,        5},
  { "lutris",   NULL,       NULL,       1 << 3,       0,           -1,    0,    50,50,500,500,        5},
  { NULL,  "youtube music",       NULL,       1 << 4,       0,           -1, 0,       50,50,500,500,        5},
  { NULL,       NULL,   "scratchpad",   0,            1,           -1,   's', 90,50,1200,400,        5,   },
  { NULL,       NULL,   "habits",   0,            1,           -1,   'h', 90,50,1200,400,        5,   },
  { NULL,       NULL,   "task-tui",   0,            1,           -1,   't', 800,50,500,600,        5,   },
  { "Noi",       NULL,   NULL,   0,            1,           -1,   'i', 800,50,500,700,        5,   },
  { NULL,       NULL,   "Kuro",   0,            1,           -1,   'k', 750,60,500,600,        5,   },
  { NULL,       NULL,   "pulsemixer",   0,            1,           -1,   'p', 800,50,800,600,        5,   },
  { NULL,       NULL,   "btop",   0,            1,           -1,   'b', 90,50,1200,600,        5,   },
  { NULL,       NULL,   "neorg",   0,            1,           -1,   'n', 90,50,1200,600,        5,   },
  { NULL,       NULL,   "tt",   0,            1,           -1,   'e', 90,50,1200,600,        5,   },
  { NULL,       NULL,   "Exercise Timer",   0,            1,           -1,   't', 500,50,400,400,        5,   },
  { NULL,       NULL,   "clock",   0,            1,           -1,   'c', 500,50,400,400,        5,   },
  { "trayer",       NULL,   "panel",   0,            1,           -1,   'q', 500,50,400,400,        5,   },
};

/* layout(s) */
static const float mfact     = 0.55; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 1;    /* 1 means respect size hints in tiled resizals */
static const int lockfullscreen = 1; /* 1 will force focus on the fullscreen window */

static const Layout layouts[] = {
	/* symbol     arrange function */
	{ "[]=",      tile },    /* first entry is default */
	{ "><>",      NULL },    /* no layout function means floating behavior */
	{ "",      monocle },
	{ "",      bstack },
	{ "===",      bstackhoriz },
};

/* custom symbols for nr. of clients in monocle layout */
/* when clients >= LENGTH(monocles), uses the last element */
static const char *monocles[] = { "A", "B", "C", "D", "F", "G", "H", "I", "J", "K+" };
/* key definitions */
#define MODKEY Mod4Mask
#define TAGKEYS(KEY,TAG)                                                                                               \
       &((Keychord){1, {{MODKEY, KEY}},                                        view,           {.ui = 1 << TAG} }), \
       &((Keychord){1, {{MODKEY|ControlMask, KEY}},                            toggleview,     {.ui = 1 << TAG} }), \
       &((Keychord){1, {{MODKEY|ShiftMask, KEY}},                              tag,            {.ui = 1 << TAG} }), \
       &((Keychord){1, {{MODKEY|ControlMask|ShiftMask, KEY}},                  toggletag,      {.ui = 1 << TAG} }),

/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

/* commands */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
//static const char *dmenucmd[] = { "dmenu_run", "-m", dmenumon, "-fn", dmenufont, "-nb", bg1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray4, NULL };
static const char *dmenucmd[] = { "dmenu_run", "-nb", "#000", "-z", "700", "-x", "230", "-y", "2", NULL };
static const char *clipmenucmd[] = { "clipmenu", "-nb", "#000", "-z", "700", "-x", "230", "-y", "4", NULL };
static const char *bass[] = { "flatpak", "run", "com.github.wwmm.easyeffects", "-l", "Heavy Bass", NULL};
static const char *loudness[] = { "flatpak", "run", "com.github.wwmm.easyeffects", "-l", "LoudnessEqualizer", NULL};
static const char *termcmd[]  = { "st", "-A", "0.50", NULL };
static const char *pymors[]  = { "pymor", NULL };
static const char *pymorl[]  = { "pymor", "-l", "3", NULL };
static const char *pymorc[]  = { "pymor", "-c", NULL };
static const char *dunst[]  = { "dunstctl", "close-all", NULL };
static const char *rotatemouse[]  = { "360.sh", "252", NULL };
static const char *volup[]  = { "volume.sh", "up", NULL };
static const char *voldw[]  = { "volume.sh", "down", NULL };
static const char *volm[]  = { "volume.sh", "mute", NULL };
/*First arg only serves to match against key in rules*/
static const char *scratchpadcmd[] = {"s", "st", "-A", "0.50", "-t", "scratchpad", NULL}; 
static const char *scratchpadclock[] = {"c", "st", "-A", "0.50", "-t", "clock", "-e", "tclock_timer.sh", NULL}; 
static const char *scratchpadhabit[] = {"h", "st", "-A", "0.70", "-t", "habits", "-e", "lvim", "/home/digo/.vimwiki/Habits.wiki", NULL}; 
static const char *scratchpadbtop[] = {"b", "st", "-t", "btop", "-e", "btop", NULL}; 
//static const char *scratchpadtask[] = {"t", "st", "-t", "task-tui", "-e", "/usr/bin/taskwarrior-tui", NULL}; 
static const char *scratchpadkuro[] = {"k", "kuro", NULL}; 
static const char *scratchpadmixer[] = {"p", "st", "-t", "pulsemixer", "-e", "pulsemixer", NULL}; 
static const char *scratchpadneorg[] = {"n", "st", "-t", "neorg", "-e", "/usr/bin/nvim -c ':Neorg workspace home'", NULL}; 
static const char *scratchpadtt[] = {"e", "st", "-t", "tt", "-e", "tt", "-t", "60", NULL}; 
static const char *scratchpadia[] = {"i", "noi", NULL}; 
static const char *scratchpadstretch[] = {"t", "flatpak", "run", "xyz.safeworlds.hiit", NULL}; 
static const char *scratchpadtrayer[] = {"q", "trayer", "--widthtype", "pixel", "--transparent", "true", "--alpha", "255", "--distance", "10", NULL}; 

static Keychord *keychords[] = {
  /* Keys        function        argument */
  &((Keychord){1, {{MODKEY, XK_p}},                                       spawn,          {.v = dmenucmd } }),
  &((Keychord){1, {{MODKEY, XK_t}},                                       spawn,          {.v = termcmd } }),
  &((Keychord){1, {{MODKEY, XK_b}},                                       togglebar,      {0} }),
  &((Keychord){1, {{MODKEY, XK_j}},                                       focusstack,     {.i = +1 } }),
  &((Keychord){1, {{MODKEY, XK_k}},                                       focusstack,     {.i = -1 } }),
  &((Keychord){1, {{MODKEY, XK_i}},                                       incnmaster,     {.i = +1 } }),
  &((Keychord){1, {{MODKEY, XK_d}},                                       incnmaster,     {.i = -1 } }),
  &((Keychord){1, {{MODKEY, XK_h}},                                       setmfact,       {.f = -0.05} }),
  // clients
  &((Keychord){3, {{MODKEY, XK_a}, {0, XK_c}, {0, XK_f}},                 togglefullscr,  {0}}),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_f}},           togglefullscr,  {0}}),
  // layouts
  &((Keychord){3, {{MODKEY, XK_a}, {0, XK_l}, {0, XK_1}},                 setlayout,  {.v = &layouts[0]}}),
  &((Keychord){3, {{MODKEY, XK_a}, {0, XK_l}, {0, XK_2}},                 setlayout,  {.v = &layouts[1]}}),
  &((Keychord){3, {{MODKEY, XK_a}, {0, XK_l}, {0, XK_t}},                 setlayout,  {.v = &layouts[2]}}),
  &((Keychord){3, {{MODKEY, XK_a}, {0, XK_l}, {0, XK_b}},                 setlayout,  {.v = &layouts[3]}}),
  &((Keychord){3, {{MODKEY, XK_a}, {0, XK_l}, {0, XK_5}},                 setlayout,  {.v = &layouts[4]}}),
  // scratchs
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_u}},                            togglescratch,  {.v = scratchpadcmd } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_m}},                            togglescratch,  {.v = scratchpadbtop } }),
  //  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_t}},                            togglescratch,  {.v = scratchpadtask } }),
//  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_s}},                            togglescratch,  {.v = scratchpadneorg } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_e}},                            togglescratch,  {.v = scratchpadtt } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_p}},                            togglescratch,  {.v = scratchpadmixer } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_t}},                            togglescratch,  {.v = scratchpadkuro } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_i}},                            togglescratch,  {.v = scratchpadia } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_c}},                            togglescratch,  {.v = scratchpadstretch } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_s}},                            togglescratch,  {.v = scratchpadtrayer } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_h}},                            togglescratch,  {.v = scratchpadhabit } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_r}},                            togglescratch,  {.v = scratchpadclock } }),
  // volume
  &((Keychord){2, {{MODKEY, XK_v}, {0, XK_j}},                            spawn,  {.v = voldw } }),
  &((Keychord){2, {{MODKEY, XK_v}, {0, XK_k}},                            spawn,  {.v = volup } }),
  &((Keychord){2, {{MODKEY, XK_v}, {0, XK_m}},                            spawn,  {.v = volm } }),
  // exec
  &((Keychord){2, {{MODKEY, XK_e}, {0, XK_r}},                            spawn,  {.v = dmenucmd } }),
  &((Keychord){2, {{MODKEY, XK_e}, {0, XK_h}},                            spawn,  {.v = clipmenucmd } }),
  &((Keychord){2, {{MODKEY, XK_e}, {0, XK_n}},                            spawn,  {.v = dunst } }),
  &((Keychord){2, {{MODKEY, XK_e}, {0, XK_m}},                            spawn,  {.v = rotatemouse } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_e}, {0, XK_b}},                 spawn,          {.v = bass } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_e}, {0, XK_l}},                 spawn,          {.v = loudness } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_p}, {0, XK_s}},                 spawn,          {.v = pymors } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_p}, {0, XK_l}},                 spawn,          {.v = pymorl } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_p}, {0, XK_c}},                 spawn,          {.v = pymorc } }),
  //rest
  &((Keychord){1, {{MODKEY, XK_l}},                                       setmfact,       {.f = +0.05} }),
  &((Keychord){1, {{MODKEY, XK_Return}},                                  zoom,           {0} }),
  &((Keychord){1, {{MODKEY, XK_Tab}},                                     view,           {0} }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_c}},                             killclient,     {0} }),
  &((Keychord){1, {{MODKEY, XK_space}},                                   setlayout,      {0} }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_space}},                         togglefloating, {0} }),
  &((Keychord){1, {{MODKEY, XK_0}},                                       view,           {.ui = ~0 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_0}},                             tag,            {.ui = ~0 } }),
  &((Keychord){1, {{MODKEY, XK_comma}},                                   focusmon,       {.i = -1 } }),
  &((Keychord){1, {{MODKEY, XK_period}},                                  focusmon,       {.i = +1 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_comma}},                         tagmon,         {.i = -1 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_period}},                        tagmon,         {.i = +1 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_q}},                             quit,           {0} }),
  TAGKEYS(                        XK_1,                      0)
  TAGKEYS(                        XK_2,                      1)
  TAGKEYS(                        XK_3,                      2)
  TAGKEYS(                        XK_4,                      3)
  TAGKEYS(                        XK_5,                      4)
  TAGKEYS(                        XK_6,                      5)
  TAGKEYS(                        XK_7,                      6)
  TAGKEYS(                        XK_8,                      7)
  TAGKEYS(                        XK_9,                      8)
};


/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static const Button buttons[] = {
	/* click                event mask      button          function        argument */
	{ ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
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

