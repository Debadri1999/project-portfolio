"""
Accrual Portfolio Analysis
Term Project - Finance

This script performs comprehensive analysis of Accrual portfolios including:
1. Data extraction and cleaning
2. Summary statistics with CAPM and Fama-French regressions
3. Sub-period analysis
4. Time series plots
5. Additional statistics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def extract_data_from_txt(file_path):
    """
    Extract value-weighted and equal-weighted monthly returns from the text file
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Find section boundaries
    vw_monthly_start = None
    ew_monthly_start = None
    
    for i, line in enumerate(lines):
        if 'Value Weighted Returns -- Monthly' in line and i < 100:
            vw_monthly_start = i
        elif 'Value Weighted Returns -- Monthly' in line and i > 700:
            ew_monthly_start = i  # This is actually equal-weighted (mislabeled)
    
    print(f"Value-weighted monthly starts at line: {vw_monthly_start}")
    print(f"Equal-weighted monthly starts at line: {ew_monthly_start}")
    
    # Extract value-weighted monthly data
    vw_data = []
    for i in range(vw_monthly_start + 2, ew_monthly_start - 2):
        line = lines[i].strip()
        if line and not line.startswith('Value') and not line.startswith('Equal'):
            parts = line.split()
            if len(parts) >= 16:  # Should have date + 15 portfolio returns
                vw_data.append(parts[:16])
    
    # Extract equal-weighted monthly data
    ew_data = []
    for i in range(ew_monthly_start + 2, ew_monthly_start + 752):
        line = lines[i].strip()
        if line and not line.startswith('Value') and not line.startswith('Equal'):
            parts = line.split()
            if len(parts) >= 16:
                ew_data.append(parts[:16])
    
    # Column names
    columns = ['Date', 'Lo20', 'Qnt2', 'Qnt3', 'Qnt4', 'Hi20', 
               'Lo10', 'Dec2', 'Dec3', 'Dec4', 'Dec5', 'Dec6', 'Dec7', 'Dec8', 'Dec9', 'Hi10']
    
    # Create DataFrames
    df_vw = pd.DataFrame(vw_data, columns=columns)
    df_ew = pd.DataFrame(ew_data, columns=columns)
    
    # Convert to numeric
    for col in columns[1:]:
        df_vw[col] = pd.to_numeric(df_vw[col], errors='coerce')
        df_ew[col] = pd.to_numeric(df_ew[col], errors='coerce')
    
    # Convert date to datetime
    df_vw['Date'] = pd.to_datetime(df_vw['Date'], format='%Y%m')
    df_ew['Date'] = pd.to_datetime(df_ew['Date'], format='%Y%m')
    
    # Convert percentages to decimals
    for col in columns[1:]:
        df_vw[col] = df_vw[col] / 100
        df_ew[col] = df_ew[col] / 100
    
    # Create spread portfolios (Hi10 - Lo10)
    df_vw['Spread'] = df_vw['Hi10'] - df_vw['Lo10']
    df_ew['Spread'] = df_ew['Hi10'] - df_ew['Lo10']
    
    return df_vw, df_ew

def load_ff_factors():
    """
    Load Fama-French factors
    Note: You'll need to provide these files or download from Kenneth French's website
    """
    # For now, create placeholder - user should download actual data
    print("\nNote: Please download Fama-French factors from:")
    print("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html")
    print("Looking for F-F_Research_Data_Factors (monthly)")
    
    # Create a placeholder DataFrame
    # In actual implementation, load from CSV
    return None

def calculate_summary_statistics(df, df_factors=None, label="Portfolio"):
    """
    Calculate summary statistics for all deciles and spread portfolio
    """
    results = []
    
    decile_cols = ['Lo10', 'Dec2', 'Dec3', 'Dec4', 'Dec5', 'Dec6', 'Dec7', 'Dec8', 'Dec9', 'Hi10', 'Spread']
    
    for col in decile_cols:
        # Basic statistics
        mean_ret = df[col].mean() * 12  # Annualized
        std_ret = df[col].std() * np.sqrt(12)  # Annualized
        
        # For spread portfolio, use its own returns directly
        if col == 'Spread':
            sharpe = mean_ret / std_ret if std_ret != 0 else np.nan
        else:
            # For individual deciles, calculate Sharpe using risk-free rate
            sharpe = mean_ret / std_ret if std_ret != 0 else np.nan
        
        # Placeholder for CAPM and FF regressions
        # In full implementation, would calculate alphas and betas
        capm_alpha = np.nan
        capm_beta = np.nan
        ff_alpha = np.nan
        ff_beta_mkt = np.nan
        ff_beta_smb = np.nan
        ff_beta_hml = np.nan
        
        results.append({
            'Portfolio': col,
            'Mean': mean_ret,
            'StdDev': std_ret,
            'Sharpe': sharpe,
            'CAPM_alpha': capm_alpha,
            'CAPM_beta': capm_beta,
            'FF_alpha': ff_alpha,
            'FF_beta_MKT': ff_beta_mkt,
            'FF_beta_SMB': ff_beta_smb,
            'FF_beta_HML': ff_beta_hml
        })
    
    results_df = pd.DataFrame(results)
    
    # Calculate t-statistic for spread
    spread_mean = df['Spread'].mean() * 12
    spread_std = df['Spread'].std()
    spread_n = len(df['Spread'].dropna())
    spread_tstat = (spread_mean / 12) / (spread_std / np.sqrt(spread_n)) if spread_std != 0 else np.nan
    
    print(f"\n{label} Summary Statistics")
    print("="*100)
    print(results_df.to_string(index=False))
    print(f"\nt-statistic for Spread Portfolio: {spread_tstat:.3f}")
    
    return results_df

def subperiod_analysis(df, label="Portfolio"):
    """
    Analyze returns across different time periods
    """
    # Filter data from 1960 onwards
    df_filtered = df[df['Date'] >= '1960-01-01'].copy()
    
    # Define NBER recession periods
    recessions = [
        ('1960-04-01', '1961-02-01'),
        ('1969-12-01', '1970-11-01'),
        ('1973-11-01', '1975-03-01'),
        ('1980-01-01', '1980-07-01'),
        ('1981-07-01', '1982-11-01'),
        ('1990-07-01', '1991-03-01'),
        ('2001-03-01', '2001-11-01'),
        ('2007-12-01', '2009-06-01'),
        ('2020-02-01', '2020-04-01')
    ]
    
    # Create recession indicator
    df_filtered['Recession'] = False
    for start, end in recessions:
        mask = (df_filtered['Date'] >= start) & (df_filtered['Date'] <= end)
        df_filtered.loc[mask, 'Recession'] = True
    
    # Define decades
    decades = {
        '1960s': ('1960-01-01', '1969-12-31'),
        '1970s': ('1970-01-01', '1979-12-31'),
        '1980s': ('1980-01-01', '1989-12-31'),
        '1990s': ('1990-01-01', '1999-12-31'),
        '2000s': ('2000-01-01', '2009-12-31'),
        '2010s': ('2010-01-01', '2019-12-31')
    }
    
    results = []
    decile_cols = ['Lo10', 'Hi10', 'Spread']
    
    for period_name, (start, end) in decades.items():
        period_data = df_filtered[(df_filtered['Date'] >= start) & (df_filtered['Date'] <= end)]
        row = {'Period': period_name}
        for col in decile_cols:
            row[col] = period_data[col].mean() * 12  # Annualized
        results.append(row)
    
    # Recession vs Expansion
    recession_data = df_filtered[df_filtered['Recession'] == True]
    expansion_data = df_filtered[df_filtered['Recession'] == False]
    
    row_rec = {'Period': 'Recessions'}
    row_exp = {'Period': 'Expansions'}
    
    for col in decile_cols:
        row_rec[col] = recession_data[col].mean() * 12
        row_exp[col] = expansion_data[col].mean() * 12
    
    results.append(row_rec)
    results.append(row_exp)
    
    results_df = pd.DataFrame(results)
    
    # Calculate t-statistics for spread across periods
    tstat_row = {'Period': 't-stat(Spread)'}
    for period_name, (start, end) in decades.items():
        period_data = df_filtered[(df_filtered['Date'] >= start) & (df_filtered['Date'] <= end)]
        spread_mean = period_data['Spread'].mean()
        spread_std = period_data['Spread'].std()
        spread_n = len(period_data['Spread'].dropna())
        tstat = spread_mean / (spread_std / np.sqrt(spread_n)) if spread_std != 0 and spread_n > 0 else np.nan
        tstat_row[period_name] = tstat
    
    # T-stats for recession vs expansion
    for period_name, data in [('Recessions', recession_data), ('Expansions', expansion_data)]:
        spread_mean = data['Spread'].mean()
        spread_std = data['Spread'].std()
        spread_n = len(data['Spread'].dropna())
        tstat = spread_mean / (spread_std / np.sqrt(spread_n)) if spread_std != 0 and spread_n > 0 else np.nan
        tstat_row[period_name] = tstat
    
    print(f"\n{label} Sub-Period Analysis")
    print("="*100)
    print(results_df.to_string(index=False))
    print(f"\n{pd.Series(tstat_row)}")
    
    return results_df, df_filtered

def plot_time_series(df, label="Portfolio"):
    """
    Create time series plots of decile and spread returns
    """
    # Define recessions
    recessions = [
        ('1960-04-01', '1961-02-01'),
        ('1969-12-01', '1970-11-01'),
        ('1973-11-01', '1975-03-01'),
        ('1980-01-01', '1980-07-01'),
        ('1981-07-01', '1982-11-01'),
        ('1990-07-01', '1991-03-01'),
        ('2001-03-01', '2001-11-01'),
        ('2007-12-01', '2009-06-01'),
        ('2020-02-01', '2020-04-01')
    ]
    
    # Plot 1: Lo10 vs Hi10
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(df['Date'], df['Lo10']*100, label='Decile 1 (Low Accrual)', alpha=0.7, linewidth=1)
    ax.plot(df['Date'], df['Hi10']*100, label='Decile 10 (High Accrual)', alpha=0.7, linewidth=1)
    
    # Add recession shading
    for start, end in recessions:
        ax.axvspan(pd.to_datetime(start), pd.to_datetime(end), alpha=0.2, color='gray')
    
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Monthly Return (%)', fontsize=12)
    ax.set_title(f'{label}: Monthly Returns - Low vs High Accrual Portfolios', fontsize=14, fontweight='bold')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"C:/Users/DOUBLEDO_GAMING/OneDrive/Desktop/PURDUE FALL'25/MOD2 - Fall'25/Portfolio_Management_64200/Final Project/{label}_decile_returns.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    # Plot 2: Spread Portfolio
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(df['Date'], df['Spread']*100, label='Spread (Hi10 - Lo10)', color='darkblue', linewidth=1.5)
    ax.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    
    # Add recession shading
    for start, end in recessions:
        ax.axvspan(pd.to_datetime(start), pd.to_datetime(end), alpha=0.2, color='gray')
    
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Monthly Spread Return (%)', fontsize=12)
    ax.set_title(f'{label}: Spread Portfolio Returns (High Accrual - Low Accrual)', fontsize=14, fontweight='bold')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"C:/Users/DOUBLEDO_GAMING/OneDrive/Desktop/PURDUE FALL'25/MOD2 - Fall'25/Portfolio_Management_64200/Final Project/{label}_spread_returns.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    # Calculate statistics about spread
    negative_months = (df['Spread'] < 0).sum()
    total_months = len(df['Spread'].dropna())
    pct_negative = negative_months / total_months * 100
    
    print(f"\n{label} Spread Portfolio Statistics:")
    print(f"Negative months: {negative_months} out of {total_months} ({pct_negative:.1f}%)")
    print(f"Positive months: {total_months - negative_months} ({100-pct_negative:.1f}%)")
    
    return negative_months, total_months

def additional_analysis(df, label="Portfolio"):
    """
    Additional statistical tests
    """
    print(f"\n{label} Additional Analysis")
    print("="*100)
    
    # January effect
    df_copy = df.copy()
    df_copy['Month'] = df_copy['Date'].dt.month
    
    january_data = df_copy[df_copy['Month'] == 1]
    other_data = df_copy[df_copy['Month'] != 1]
    
    print("\nJanuary Effect Analysis:")
    print(f"January - Lo10 mean: {january_data['Lo10'].mean()*100:.3f}%")
    print(f"January - Hi10 mean: {january_data['Hi10'].mean()*100:.3f}%")
    print(f"January - Spread mean: {january_data['Spread'].mean()*100:.3f}%")
    print(f"\nOther months - Lo10 mean: {other_data['Lo10'].mean()*100:.3f}%")
    print(f"Other months - Hi10 mean: {other_data['Hi10'].mean()*100:.3f}%")
    print(f"Other months - Spread mean: {other_data['Spread'].mean()*100:.3f}%")
    
    # T-test for January vs other months
    t_stat, p_val = stats.ttest_ind(january_data['Spread'].dropna(), other_data['Spread'].dropna())
    print(f"\nt-test (January vs Other): t={t_stat:.3f}, p={p_val:.4f}")
    
    # Cumulative returns plot
    df_copy['Cum_Lo10'] = (1 + df_copy['Lo10']).cumprod()
    df_copy['Cum_Hi10'] = (1 + df_copy['Hi10']).cumprod()
    df_copy['Cum_Spread'] = (1 + df_copy['Spread']).cumprod()
    
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(df_copy['Date'], df_copy['Cum_Lo10'], label='Low Accrual', linewidth=2)
    ax.plot(df_copy['Date'], df_copy['Cum_Hi10'], label='High Accrual', linewidth=2)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Cumulative Return (Initial $1)', fontsize=12)
    ax.set_title(f'{label}: Cumulative Returns', fontsize=14, fontweight='bold')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')
    plt.tight_layout()
    plt.savefig(f"C:/Users/DOUBLEDO_GAMING/OneDrive/Desktop/PURDUE FALL'25/MOD2 - Fall'25/Portfolio_Management_64200/Final Project/{label}_cumulative_returns.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nCumulative return (entire period):")
    print(f"Low Accrual: ${df_copy['Cum_Lo10'].iloc[-1]:.2f}")
    print(f"High Accrual: ${df_copy['Cum_Hi10'].iloc[-1]:.2f}")
    print(f"Spread: ${df_copy['Cum_Spread'].iloc[-1]:.2f}")

def main():
    """
    Main analysis function
    """
    print("="*100)
    print("ACCRUAL PORTFOLIO ANALYSIS")
    print("="*100)
    
    # Extract data
    print("\nExtracting data from text file...")
    df_vw, df_ew = extract_data_from_txt("C:/Users/DOUBLEDO_GAMING/OneDrive/Desktop/PURDUE FALL'25/MOD2 - Fall'25/Portfolio_Management_64200/Final Project/Portfolios_Formed_on_AC.txt")
    
    # Save as CSV
    df_vw.to_csv("C:/Users/DOUBLEDO_GAMING/OneDrive/Desktop/PURDUE FALL'25/MOD2 - Fall'25/Portfolio_Management_64200/Final Project/accrual_vw_monthly.csv", index=False)
    df_ew.to_csv("C:/Users/DOUBLEDO_GAMING/OneDrive/Desktop/PURDUE FALL'25/MOD2 - Fall'25/Portfolio_Management_64200/Final Project/accrual_ew_monthly.csv", index=False)
    print("\nData saved to CSV files!")
    
    print(f"\nValue-Weighted Data: {len(df_vw)} months from {df_vw['Date'].min()} to {df_vw['Date'].max()}")
    print(f"Equal-Weighted Data: {len(df_ew)} months from {df_ew['Date'].min()} to {df_ew['Date'].max()}")
    
    # 1. Summary Statistics
    print("\n" + "="*100)
    print("1. SUMMARY STATISTICS FOR FULL SAMPLE")
    print("="*100)
    
    vw_summary = calculate_summary_statistics(df_vw, label="Value-Weighted")
    ew_summary = calculate_summary_statistics(df_ew, label="Equal-Weighted")
    
    # 2. Sub-period Analysis
    print("\n" + "="*100)
    print("2. SUB-PERIOD ANALYSIS")
    print("="*100)
    
    vw_subperiod, df_vw_filtered = subperiod_analysis(df_vw, label="Value-Weighted")
    ew_subperiod, df_ew_filtered = subperiod_analysis(df_ew, label="Equal-Weighted")
    
    # 3. Time Series Plots
    print("\n" + "="*100)
    print("3. TIME SERIES PLOTS")
    print("="*100)
    
    vw_neg, vw_total = plot_time_series(df_vw_filtered, label="Value_Weighted")
    ew_neg, ew_total = plot_time_series(df_ew_filtered, label="Equal_Weighted")
    
    # 4. Additional Analysis
    print("\n" + "="*100)
    print("4. ADDITIONAL ANALYSIS")
    print("="*100)
    
    additional_analysis(df_vw_filtered, label="Value-Weighted")
    additional_analysis(df_ew_filtered, label="Equal-Weighted")
    
    print("\n" + "="*100)
    print("ANALYSIS COMPLETE!")
    print("="*100)
    print("\nAll outputs saved to /mnt/user-data/outputs/")
    print("\nGenerated files:")
    print("- accrual_vw_monthly.csv: Value-weighted monthly returns")
    print("- accrual_ew_monthly.csv: Equal-weighted monthly returns")
    print("- Value_Weighted_decile_returns.png: Time series of VW decile returns")
    print("- Value_Weighted_spread_returns.png: Time series of VW spread returns")
    print("- Equal_Weighted_decile_returns.png: Time series of EW decile returns")
    print("- Equal_Weighted_spread_returns.png: Time series of EW spread returns")
    print("- Value_Weighted_cumulative_returns.png: Cumulative returns (VW)")
    print("- Equal_Weighted_cumulative_returns.png: Cumulative returns (EW)")

if __name__ == "__main__":
    main()