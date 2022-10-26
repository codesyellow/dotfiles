/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 1;        /* border pixel of windows */
static const unsigned int snap      = 32;       /* snap pixel */
static const unsigned int systraypinning = 0;   /* 0: sloppy systray follows selected monitor, >0: pin systray to monitor X */
static const unsigned int systrayonleft = 0;   	/* 0: systray in the right corner, >0: systray on left of status text */
static const unsigned int systrayspacing = 2;   /* systray spacing */
static const int systraypinningfailfirst = 1;   /* 1: if pinning fails, display systray on the first monitor, False: display systray on the last monitor*/
static const int showsystray        = 1;     /* 0 means no systray */
static const int showbar            = 1;     /* 0 means no bar */
static const int topbar             = 1;     /* 0 means bottom bar */
static const char *fonts[]          = { 
  "CaskadiaCove Nerd Font:size=10",
  "Font Awesome 6 Free Solid:size=10",
  "Font Awesome 6 Free Regular:size=10",
  "Font Awesome 6 Brands:size=10"
   };
static const char dmenufont[]       = "CaskadiaCove Nerd Font:size=12";
static const char col_gray1[]       = "#2e3440";
static const char col_gray2[]       = "#bf616a";
static const char col_gray3[]       = "#999999";
static const char col_gray4[]       = "#ffffff";
static const char col_cyan[]        = "#88c0d0";
static const char *colors[][3]      = {
	/*               fg         bg         border   */
	[SchemeNorm] = { col_gray3, col_gray1, col_gray2 },
	[SchemeSel]  = { col_gray4, col_cyan,  col_cyan  },
};

/* tagging */
static const char *tags[] = { "", " ", "", "", "", "", "", "" };

static const Rule rules[] = {
	/* xprop(1):
	 *	WM_CLASS(STRING) = instance, class
	 *	WM_NAME(STRING) = title
	 */
	/* class      instance    title       tags mask     isfloating   monitor    float x,y,w,h         floatborderpx*/
	{ "Gimp",     NULL,       NULL,       0,            1,           -1,        50,50,500,500,        5 },
	{ "st-256color",  NULL,       NULL,       1 << 6,       0,           -1,        50,50,1200,400,        5 },
	{ "firefox",  NULL,       NULL,       1 << 1,       0,           -1,        50,50,500,500,        5 },
	{ "YouTube Music",  NULL,       NULL,       1 << 2,       0,           -1,        50,50,500,500,        5 },
	/* class      instance    title       tags mask     isfloating   monitor    scratch key */
	{ NULL,       NULL,   "scratchpad",   0,           1,           -1,          's',         70,50,1200,300,        5 },
	{ "btop",     NULL,       NULL,   0,            1,           -1,          'b',         70,50,1200,600,        5 },
};

/* layout(s) */
static const float mfact     = 0.65; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 1;    /* 1 means respect size hints in tiled resizals */
static const int lockfullscreen = 1; /* 1 will force focus on the fullscreen window */

static const Layout layouts[] = {
	/* symbol     arrange function */
	{ "|    ",      bstack },
	{ "|    ",      monocle },
	{ "|    ",      NULL },    /* no layout function means floating behavior */
};

/* key definitions */
#define MODKEY Mod3Mask
#define TAGKEYS(KEY,TAG)												\
	&((Keychord){1, {{MODKEY, KEY}},								view,           {.ui = 1 << TAG} }), \
		&((Keychord){1, {{MODKEY|ControlMask, KEY}},					toggleview,     {.ui = 1 << TAG} }), \
		&((Keychord){1, {{MODKEY|ShiftMask, KEY}},						tag,            {.ui = 1 << TAG} }), \
		&((Keychord){1, {{MODKEY|ControlMask|ShiftMask, KEY}},			toggletag,      {.ui = 1 << TAG} }),

/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

// apps
static const char *dmenucmd[] = { "dmenu_run", "-fn", dmenufont, "-nb", col_gray1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray4, NULL };
static const char *termcmd[]  = { "st", NULL };
// cli
static const char *volup[]  = { "volume.sh", "up", NULL };
static const char *voldw[]  = { "volume.sh", "down", NULL };
static const char *loudness[]  = { "easyeffects", "-l", "LoudnessEqualizer", NULL };
static const char *music[]  = { "easyeffects", "-l", "Heavy Bass", NULL };
// scratchpad
static const char *scratchpadcmd[] = {"s", "st", "-A", ".6", "-t", "scratchpad", NULL}; 
static const char *scratchpadbtop[] = {"b", "st", "-c", "btop", "btop", NULL}; 

static Keychord *keychords[] = {
	/* Keys        function        argument */
	&((Keychord){1, {{MODKEY, XK_d}},							spawn,          {.v = dmenucmd } }),
	&((Keychord){1, {{MODKEY, XK_t}},			        spawn,          {.v = termcmd } }),
	&((Keychord){2, {{MODKEY, XK_e}, {0, XK_e}},	spawn,          {.v = termcmd } }),

  // scratchpad
	&((Keychord){2, {{MODKEY, XK_s}, {0, XK_u}},	togglescratch,  {.v = scratchpadcmd } }),
	&((Keychord){2, {{MODKEY, XK_s}, {0, XK_b}},	togglescratch,  {.v = scratchpadbtop } }),

  // scripts
	&((Keychord){1, {{MODKEY|ShiftMask, XK_a}},		spawn,          {.v = volup} }),
	&((Keychord){1, {{MODKEY|ShiftMask, XK_d}},		spawn,          {.v = voldw} }),

  // cli
	&((Keychord){2, {{MODKEY, XK_a}, {0, XK_l}},	spawn,          {.v = loudness } }),
	&((Keychord){2, {{MODKEY, XK_a}, {0, XK_m}},	spawn,          {.v = music } }),

	&((Keychord){1, {{MODKEY, XK_b}},							togglebar,      {0} }),
	&((Keychord){1, {{MODKEY, XK_j}},							focusstack,     {.i = +1 } }),
	&((Keychord){1, {{MODKEY, XK_k}},							focusstack,     {.i = -1 } }),
	&((Keychord){1, {{MODKEY, XK_h}},							setmfact,       {.f = -0.05} }),
	&((Keychord){1, {{MODKEY, XK_l}},							setmfact,       {.f = +0.05} }),
	&((Keychord){1, {{MODKEY, XK_space}},				  zoom,           {0} }),
	&((Keychord){1, {{MODKEY, XK_Tab}},						view,           {0} }),
	&((Keychord){1, {{MODKEY|ShiftMask, XK_c}},		killclient,     {0} }),
	&((Keychord){1, {{MODKEY, XK_8}},							setlayout,      {.v = &layouts[0]} }),
	&((Keychord){1, {{MODKEY, XK_9}},							setlayout,      {.v = &layouts[1]} }),
	&((Keychord){1, {{MODKEY, XK_0}},							setlayout,      {.v = &layouts[2]} }),
	&((Keychord){1, {{MODKEY, XK_f}},					    setlayout,      {0} }),
	&((Keychord){1, {{MODKEY|ShiftMask, 
      XK_space}},				                        togglefloating, {0} }),
	&((Keychord){1, {{MODKEY|ShiftMask, XK_f}},		togglefullscr,  {0} }),
	&((Keychord){1, {{MODKEY, XK_0}},							view,           {.ui = ~0 } }),
	&((Keychord){1, {{MODKEY|ShiftMask, XK_0}},		tag,            {.ui = ~0 } }),
	&((Keychord){1, {{MODKEY, XK_comma}},					focusmon,       {.i = -1 } }),
	&((Keychord){1, {{MODKEY, XK_period}},				focusmon,       {.i = +1 } }),
	&((Keychord){1, {{MODKEY|ShiftMask, 
      XK_comma}},				                        tagmon,         {.i = -1 } }),
	&((Keychord){1, {{MODKEY|ShiftMask, 
      XK_period}},			                        tagmon,         {.i = +1 } }),
	TAGKEYS(                        XK_1,                      0)
	TAGKEYS(                        XK_2,                      1)
	TAGKEYS(                        XK_3,                      2)
	TAGKEYS(                        XK_4,                      3)
	TAGKEYS(                        XK_e,                      4)
	TAGKEYS(                        XK_i,                      5)
	TAGKEYS(                        XK_q,                      6)
	TAGKEYS(                        XK_g,                      7)
	&((Keychord){1, {{MODKEY|ShiftMask, XK_q}},					quit,           {0} }),
};

/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static const Button buttons[] = {
	/* click                event mask      button          function        argument */
	{ ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
	{ ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
	{ ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
	{ ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
	{ ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
	{ ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
	{ ClkTagBar,            0,              Button1,        view,           {0} },
	{ ClkTagBar,            0,              Button3,        toggleview,     {0} },
	{ ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
	{ ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
};

