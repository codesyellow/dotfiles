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
  "CaskadiaCove Nerd Font:size=10",
  "Font Awesome 6 Free Solid:size=10",
  "Font Awesome 6 Free Regular:size=10",
  "Font Awesome 6 Brands:size=10"
   };
static const char dmenufont[]       = "monospace:size=10";
static const char col_gray1[]       = "#222222";
static const char col_gray2[]       = "#444444";
static const char col_gray3[]       = "#bbbbbb";
static const char col_gray4[]       = "#eeeeee";
static const char col_cyan[]        = "#005577";
static const char *colors[][3]      = {
	/*               fg         bg         border   */
	[SchemeNorm] = { col_gray3, col_gray1, col_gray2 },
	[SchemeSel]  = { col_gray4, col_cyan,  col_cyan  },
};

/* tagging */
static const char *tags[] = { "1", "2", "3", "4", "5", "6" };
static const int taglayouts[] = { 0, 0, 3, 0, 2, 0  };

static const Rule rules[] = {
	/* xprop(1):
	 *	WM_CLASS(STRING) = instance, class
	 *	WM_NAME(STRING) = title
	 */
	/* class      instance    title       tags mask     isfloating   monitor    float x,y,w,h         floatborderpx*/
	{ "Gimp",     NULL,       NULL,       0,            1,           -1,   0,     50,50,500,500,        5 },
	{ "firefox",  NULL,       NULL,       1 << 1,       0,           -1,   0,     50,50,500,500,        5 },
	{ "st-256color",  NULL,       NULL,       1 << 2,       0,           -1,   0,     50,50,500,500,        5 },
  { "Alacritty",NULL,       NULL,       1 << 1,       0,           -1,        50,50,500,500,        5,      0},
  { "Zathura",  NULL,       NULL,       1 << 3,       0,           -1,        50,50,500,500,        5,      0},
  { "steam",    "steamwebhelper",       NULL,       1 << 4,       0,           -1,        50,50,500,500,        5,      0},
  { NULL,    NULL,       "Steam",       1 << 4,       0,           -1,        50,50,500,500,        5,      0},
  { NULL,    NULL,       "Steam setup",       1 << 4,       0,           -1,        50,50,500,500,        5,      0},
  { "heroic",   NULL,       NULL,       1 << 4,       0,           -1,        50,50,500,500,        5,      0},
  { NULL,  "youtube music",       NULL,       1 << 5,       0,           -1,        50,50,500,500,        5,      0},
  { NULL,       NULL,   "scratchpad",   0,            1,           -1,   's', 90,50,1200,400,        5,   },
  { NULL,       NULL,   "task-tui",   0,            1,           -1,   't', 800,50,500,600,        5,   },
  { NULL,       NULL,   "pulsemixer",   0,            1,           -1,   'p', 800,50,800,600,        5,   },
  { NULL,       NULL,   "btop",   0,            1,           -1,   'b', 90,50,1200,600,        5,   },
  { NULL,       NULL,   "neorg",   0,            1,           -1,   'n', 90,50,1200,600,        5,   },
  { NULL,       NULL,   "tt",   0,            1,           -1,   'e', 90,50,1200,600,        5,   },
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
	{ "",      monocle },
	{ "TTT",      bstack },
	{ "===",      bstackhoriz },
};

/* custom symbols for nr. of clients in monocle layout */
/* when clients >= LENGTH(monocles), uses the last element */
static const char *monocles[] = { "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]", "[9+]" };

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
static const char *dmenucmd[] = { "dmenu_run", "-m", dmenumon, "-fn", dmenufont, "-nb", col_gray1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray4, NULL };
static const char *bass[] = { "flatpak", "run", "com.github.wwmm.easyeffects", "-l", "my-heavy-bass", NULL};
static const char *loudness[] = { "flatpak", "run", "com.github.wwmm.easyeffects", "-l", "LoudnessEqualizer", NULL};
static const char *termcmd[]  = { "st", "-A", "0.70", NULL };
/*First arg only serves to match against key in rules*/
static const char *scratchpadcmd[] = {"s", "alacritty", "--config-file", "/home/cie/.config/alacritty/alacritty2.toml", "-t" "scratchpad", NULL}; 
static const char *scratchpadbtop[] = {"b", "st", "-t", "btop", "-e", "btop", NULL}; 
static const char *scratchpadtask[] = {"t", "st", "-t", "task-tui", "-e", "/usr/bin/taskwarrior-tui", NULL}; 
static const char *scratchpadmixer[] = {"p", "st", "-t", "pulsemixer", "-e", "/usr/local/bin/pulsemixer", NULL}; 
static const char *scratchpadneorg[] = {"n", "st", "-t", "neorg", "-e", "/usr/bin/nvim -c ':Neorg workspace home'", NULL}; 
static const char *scratchpadtt[] = {"e", "st", "-t", "tt", "-e", "tt", "-t", "60", NULL}; 

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
  &((Keychord){3, {{MODKEY, XK_a}, {0, XK_c}, {0, XK_f}},                  togglefullscr,  {0}}),

  // scratchs
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_u}},                            togglescratch,  {.v = scratchpadcmd } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_b}},                            togglescratch,  {.v = scratchpadbtop } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_t}},                            togglescratch,  {.v = scratchpadtask } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_i}},                            togglescratch,  {.v = scratchpadneorg } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_e}},                            togglescratch,  {.v = scratchpadtt } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_p}},                            togglescratch,  {.v = scratchpadmixer } }),

  // exec
  &((Keychord){2, {{MODKEY, XK_e}, {0, XK_r}},                            spawn,  {.v = dmenucmd } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_e}, {0, XK_b}},                                       spawn,          {.v = bass } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_e}, {0, XK_l}},                                       spawn,          {.v = loudness } }),

  &((Keychord){1, {{MODKEY, XK_l}},                                       setmfact,       {.f = +0.05} }),
  &((Keychord){1, {{MODKEY, XK_Return}},                                  zoom,           {0} }),
  &((Keychord){1, {{MODKEY, XK_Tab}},                                     view,           {0} }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_c}},                             killclient,     {0} }),
  &((Keychord){1, {{MODKEY, XK_t}},                                       setlayout,      {.v = &layouts[0]} }),
  &((Keychord){1, {{MODKEY, XK_f}},                                       setlayout,      {.v = &layouts[1]} }),
  &((Keychord){1, {{MODKEY, XK_m}},                                       setlayout,      {.v = &layouts[2]} }),
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

